from django.urls import path
from studentapp import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('create/',views.create_student,name='create'),
]