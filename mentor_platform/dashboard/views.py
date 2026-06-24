from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assessments.models import AssessmentResult
from placements.models import PlacementApplication
from roadmaps.models import LearningRoadmap

@login_required
def home(request):
    user = request.user
    recent_results = AssessmentResult.objects.filter(user=user).order_by('-completed_at')[:5]
    applications = PlacementApplication.objects.filter(user=user)
    roadmap = LearningRoadmap.objects.filter(user=user).order_by('-created_at').first()

    stats = {
        'total_assessments': AssessmentResult.objects.filter(user=user).count(),
        'total_applications': applications.count(),
        'offers_received': applications.filter(status='offer').count(),
        'roadmap_progress': roadmap.completion_percentage if roadmap else 0,
    }

    context = {
        'user': user,
        'recent_results': recent_results,
        'applications': applications[:5],
        'stats': stats,
        'roadmap': roadmap,
    }
    return render(request, 'dashboard/home.html', context)
