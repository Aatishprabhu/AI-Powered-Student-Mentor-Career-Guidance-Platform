from django.urls import path
from . import views

app_name = 'roadmaps'

urlpatterns = [
    path('generate/<int:skill_id>/', views.generate_roadmap, name='generate'),
]
