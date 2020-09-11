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
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.AssignmentView.as_view(), name='index'),
    path('<int:pk>/Assignment', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]