from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.info, name='info'),
    # path('index2', views.index, name='index2'),
]