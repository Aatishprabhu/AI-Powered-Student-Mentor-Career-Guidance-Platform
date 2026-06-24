from django.db import models
from accounts.models import CustomUser

class MentorChat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class InterviewQuestion(models.Model):
    DOMAIN_CHOICES = [
        ('dsa', 'Data Structures & Algorithms'),
        ('web', 'Web Development'),
        ('system_design', 'System Design'),
        ('behavioral', 'Behavioral'),
        ('database', 'Database'),
        ('python', 'Python'),
    ]
    domain = models.CharField(max_length=30, choices=DOMAIN_CHOICES)
    question = models.TextField()
    difficulty = models.CharField(max_length=15, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    sample_answer = models.TextField(blank=True)

class InterviewPractice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(InterviewQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField()
    ai_feedback = models.TextField()
    ai_score = models.IntegerField()  # 1-10
    practiced_at = models.DateTimeField(auto_now_add=True)
 
