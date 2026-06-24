from django.shortcuts import render

import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from assessments.models import Skill, AssessmentResult
from mentor.ai_utils import get_gemini_response
from .models import LearningRoadmap, RoadmapWeek

@login_required
def generate_roadmap(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    user = request.user

    
    result = AssessmentResult.objects.filter(user=user, assessment__skill=skill).order_by('-completed_at').first()
    level = result.level if result else 'beginner'

    prompt = f"""
    Create a detailed 8-week learning roadmap for a {level}-level student learning {skill.name}.

    Return ONLY a valid JSON array with this exact structure:
    [
        {{
            "week": 1,
            "title": "Week title",
            "topics": ["topic1", "topic2", "topic3"],
            "resources": ["resource1", "resource2"],
            "project": "Mini project idea"
        }}
    ]
    """

    raw = get_gemini_response(prompt)
    raw = raw.replace('```json', '').replace('```', '').strip()
    roadmap_data = json.loads(raw)

    
    roadmap = LearningRoadmap.objects.create(
        user=user,
        skill=skill,
        level=level,
        roadmap_data=roadmap_data
    )

    for week_data in roadmap_data:
        RoadmapWeek.objects.create(
            roadmap=roadmap,
            week_number=week_data['week'],
            title=week_data['title'],
            topics=json.dumps(week_data['topics']),
            resources=json.dumps(week_data['resources'])
        )

    return redirect('roadmaps:detail', pk=roadmap.pk) 
