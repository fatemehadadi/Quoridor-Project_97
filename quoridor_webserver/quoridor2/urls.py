from django.urls import path

from quoridor2 import views

urlpatterns = [

    path('quoridor2/', views.set_play, name='set_play'),

]
