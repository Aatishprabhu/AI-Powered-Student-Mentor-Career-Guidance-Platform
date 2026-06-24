from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('', views.assessment_list, name='list'),
    path('take/<int:assessment_id>/', views.take_assessment, name='take'),
    path('result/<int:result_id>/', views.assessment_result, name='result'),
]
