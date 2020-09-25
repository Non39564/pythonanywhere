from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'myweb'
urlpatterns = [
    path('', views.index, name='index'),
    path("register19/",views.register19, name="register"),
    path('admin/', admin.site.urls),
    path('questionnaire/', views.show_permissions, name='show_permissions'),
    #ใช้ 'localhost/myweb/accounts/'
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.AssignmentView.as_view(), name='index'),
    #path('<int:pk>/Assignment', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #ใช้ 'localhost/myweb/4/vote'
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #ใช้ 'localhost/myweb/detail/4/'
    path('detail/<int:question_id>/',views.detail),
    path("lastuser/",views.showusername),
    path("feedback/", views.feedback_form, name='home'),
]