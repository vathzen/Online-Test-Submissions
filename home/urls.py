from django.urls import path
from . import views

app_name = 'OnlineTest'

urlpatterns = [
    path('', views.index, name='index')
]