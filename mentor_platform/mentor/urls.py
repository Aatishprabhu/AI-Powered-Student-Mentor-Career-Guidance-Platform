from django.urls import path
from . import views

app_name = 'mentor'

urlpatterns = [
    path('', views.mentor_chat_view, name='chat'),
    path('send/', views.send_message, name='send_message'),
    path('resume/', views.resume_analyzer_view, name='resume'),
    path('evaluate/', views.evaluate_answer, name='evaluate_answer'),
]
