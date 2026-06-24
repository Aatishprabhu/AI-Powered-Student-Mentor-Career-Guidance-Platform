from django.db import models
  
from django.db import models
from assessments.models import Skill

class Project(models.Model):
    LEVEL_CHOICES = [('beginner','Beginner'),('intermediate','Intermediate'),('advanced','Advanced')]
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.ManyToManyField(Skill)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    estimated_hours = models.IntegerField()
    github_template = models.URLField(blank=True)
    resources = models.TextField(blank=True)  # JSON list of links

    def __str__(self):
        return self.title
