from django.contrib import admin
from django.urls import path, include
from myweb import views
from myweb.views import email_list_signup
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('myweb/', include('myweb.urls', namespace="myweb")),
    path('united', views.united),
    #ใช้ 'localhost/united'
    path('united', views.united),
    #ใช้ 'localhost/covid19'
    path('covid19',views.covid19),
    path('mapcovid19',views.mapcovid19),
    path('report19',views.report19),
    path('Login19',views.login19),
    path('register19',views.register19),
    path("logout", views.logout19, name="logout"),
    path('admin/', admin.site.urls),
    path('questionnaire',views.questionnaire),
    path('Assignment',views.Assignment),
    path('lastuser',views.showusername),
    path('feedback',views.feedback_form),
    path('email-signup/', email_list_signup, name='email-list-signup'),
    #url(r'^myweb/', include('myweb.urls', namespace="myweb")),
]
