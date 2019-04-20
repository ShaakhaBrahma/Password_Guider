from django.contrib import admin
from django.urls import path,include
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.view, name='view'),
	path('display/', views.display, name='display'),

]