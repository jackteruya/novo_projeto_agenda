from django.urls import path
from contatos import views


urlpatterns = [
    path('', views.index, name='index'),
]
