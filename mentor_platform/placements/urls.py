from django.urls import path
from . import views

app_name = 'placements'

urlpatterns = [
    path('', views.application_list, name='list'),
    path('add/', views.add_application, name='add'),
    path('update/<int:app_id>/', views.update_status, name='update_status'),
]
