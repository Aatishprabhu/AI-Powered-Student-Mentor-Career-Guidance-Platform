from django.db import models

from django.db import models
from accounts.models import CustomUser

class Skill(models.Model):
    name = models.CharField(max_length=100)  # e.g. Python, React, DSA
    category = models.CharField(max_length=100)  # e.g. Programming, Design
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Assessment(models.Model):
    title = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    duration_minutes = models.IntegerField(default=30)
    total_marks = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option_a = models.CharField(max_length=300)
    option_b = models.CharField(max_length=300)
    option_c = models.CharField(max_length=300)
    option_d = models.CharField(max_length=300)
    correct_option = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    marks = models.IntegerField(default=1)

class AssessmentResult(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    completed_at = models.DateTimeField(auto_now_add=True)

    def determine_level(self):
        percentage = (self.score / self.assessment.total_marks) * 100
        if percentage >= 75:
            return 'advanced'
        elif percentage >= 45:
            return 'intermediate'
        return 'beginner'
