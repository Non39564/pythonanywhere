from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Question, Choice, displayusername, Signup
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import FeedbackForm, EmailSignupForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
import json
import requests

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def united(req):
	return render(req, 'myweb/united.html')

def covid19(req):
    return render(req, 'myweb/covid19.html')

def mapcovid19(req):
    return render(req, 'myweb/mapcovid19.html')

def report19(req):
    return render(req, 'myweb/report19.html')

def Login19(req):
    return render(req, 'myweb/Login19.html')

def questionnaire(req):
    return render(req, 'myweb/questionnaire.html')

def showusername(req):
    displaynames=User.objects.all()
    form = EmailSignupForm()
    context = {
        'displayusername':displaynames,
        'form': form
    }
    return render(req, 'myweb/lastuser.html', context)

def register19(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f"New account created: {username}")
            login(req, user)
            return redirect("/questionnaire")

        else:
            for msg in form.error_messages:
                messages.error(req, f"{msg}: {form.error_messages[msg]}")

            return render(req,
                          template_name = "myweb/register19.html",
                          context={"form":form})
    form = UserCreationForm(req.POST)
    return render(req,
                template_name = "myweb/register19.html",
                context={"form":form})

def login19(req):
    if req.method == "POST":
        form = AuthenticationForm(req, data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req, user)
                messages.info(req, f"You are now logged in as {username}")
                return redirect('/questionnaire')
            else:
                messages.error(req, "Invalid username or password.")
        else:
            messages.error(req, "Invalid username or password.")
    form = AuthenticationForm()
    return render(req,
                  template_name = "myweb/Login19.html",
                  context={"form":form})

def Assignment(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(req, 'myweb/Assignment.html', context)

def show_permissions(req):
    if req.user.is_authenticate:
        return render(req, 'myweb/Login19.html')
    else:
        return render(req, 'myweb/questionnaire.html')

def logout19(req):
    logout(req)
    messages.info(req, "Logged out successfully!")
    return redirect("/covid19")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myweb/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myweb/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myweb/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myweb:results', args=(question.id,)))

class AssignmentView(generic.ListView):
    template_name = 'myweb/Assignment.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'myweb/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'myweb/results.html'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID
api_url= f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

def subscribe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = Signup.objects.filter(email=form.instance.email)
            if email_signup_qs.exists():
                messages.info(request, "You are already subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'myweb/thanks.html')
    else:
        form = FeedbackForm()
        context = {
        'form': form
    }
    return render(request, 'myweb/feedback_form.html', context)