from django.db import models

from django.db import models
from accounts.models import CustomUser
from assessments.models import Skill

class LearningRoadmap(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.CharField(max_length=20)
    roadmap_data = models.JSONField()  # Stores weekly plan as JSON
    completion_percentage = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

class RoadmapWeek(models.Model):
    roadmap = models.ForeignKey(LearningRoadmap, on_delete=models.CASCADE, related_name='weeks')
    week_number = models.IntegerField()
    title = models.CharField(max_length=200)
    topics = models.TextField()
    resources = models.TextField()
    is_completed = models.BooleanField(default=False) 
