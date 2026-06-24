from django.urls import path
from . import views

app_name = 'analytics'

urlpatterns = [
    path('progress-data/', views.progress_data, name='progress_data'),
]
