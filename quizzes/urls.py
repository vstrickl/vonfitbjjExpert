from django.urls import path

from . import views

# Create your URL Paths here.
urlpatterns = [
    path('', views.quiz_i, name='quizzes'),
]