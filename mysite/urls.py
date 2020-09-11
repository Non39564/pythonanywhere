from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from myweb import views

urlpatterns = [
    path('', views.index),
    path('myweb/', include('myweb.urls', namespace="myweb")),
    path('united', views.united),
    path('covid19',views.covid19),
    path('mapcovid19',views.mapcovid19),
    path('report19',views.report19),
    path('Login19',views.login19),
    path('register19',views.register19),
    path("logout", views.logout19, name="logout"),
    path('admin/', admin.site.urls),
    path('questionnaire',views.questionnaire),
    path('Assignment',views.Assignment),
    url(r'^myweb/', include('myweb.urls', namespace="myweb")),
]
