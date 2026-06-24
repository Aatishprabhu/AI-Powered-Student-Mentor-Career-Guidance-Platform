from django.shortcuts import render

import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from assessments.models import AssessmentResult
from placements.models import PlacementApplication

@login_required
def progress_data(request):
    user = request.user
    results = AssessmentResult.objects.filter(user=user).select_related('assessment__skill').order_by('completed_at')

    total_assessments = results.count()
    average_score = 0
    latest_level = 'N/A'
    level_counts = {'beginner': 0, 'intermediate': 0, 'advanced': 0}
    skill_scores = {}
    skill_counts = {}
    score_series = []

    for result in results:
        percentage = round((result.score / result.assessment.total_marks) * 100, 1)
        item = {
            'date': result.completed_at.strftime('%b %d'),
            'assessment': result.assessment.title,
            'skill': result.assessment.skill.name,
            'score_pct': percentage,
            'level': result.get_level_display(),
        }
        score_series.append(item)

        level_counts[result.level] += 1
        skill_scores.setdefault(result.assessment.skill.name, 0)
        skill_counts.setdefault(result.assessment.skill.name, 0)
        skill_scores[result.assessment.skill.name] += percentage
        skill_counts[result.assessment.skill.name] += 1

    if total_assessments:
        average_score = round(sum(item['score_pct'] for item in score_series) / total_assessments, 1)
        latest_level = score_series[-1]['level']

    skill_performance = [
        {
            'skill': skill,
            'avg_score': round(skill_scores[skill] / skill_counts[skill], 1),
            'attempts': skill_counts[skill],
        }
        for skill in skill_scores
    ]
    skill_performance.sort(key=lambda x: x['avg_score'], reverse=True)

    applications = PlacementApplication.objects.filter(user=user)
    placement_data = {
        'applied': applications.filter(status='applied').count(),
        'interview': applications.filter(status='interview').count(),
        'offer': applications.filter(status='offer').count(),
        'rejected': applications.filter(status='rejected').count(),
    }

    context = {
        'total_assessments': total_assessments,
        'average_score': average_score,
        'latest_level': latest_level,
        'level_counts': level_counts,
        'skill_performance': skill_performance,
        'score_series': score_series,
        'placement_data': placement_data,
        'recent_results': score_series[-5:][::-1],
    }

    return render(request, 'analytics/progress_data.html', context)
