from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('too', views.too),
    path('tre', views.tre),
    path('def', views.defold)


]