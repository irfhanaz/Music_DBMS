from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "App"

urlpatterns = [
    path(r'', views.index, name='index'),
	path(r'searchpage/',views.index2,name='index2'),
	path(r'songupload/',views.index3,name='index3'),
	path(r'searchpage/search/', views.search , name = "search"),
	url(r'add/', views.add , name = "add"),
	url(r'songs/',views.view, name="view"),
    path(r'play/', views.play, name="play"),
]