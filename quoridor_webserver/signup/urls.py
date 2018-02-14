from django.urls import path

from signup import views

urlpatterns = [

    path('signup/', views.index, name='index'),

]
