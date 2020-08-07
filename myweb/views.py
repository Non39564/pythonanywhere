from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def united(req):
	return render(req, 'myweb/united.html')

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objests.filter(question=question)
    return render(request, 'myweb/detail.html',{'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)