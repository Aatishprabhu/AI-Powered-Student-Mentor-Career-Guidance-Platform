import json
from pathlib import Path
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Assessment, Question, AssessmentResult, Skill

SAMPLE_ASSESSMENTS_FILE = Path(__file__).resolve().parent / 'sample_assessments.json'


def load_sample_assessments():
    if SAMPLE_ASSESSMENTS_FILE.exists():
        try:
            with SAMPLE_ASSESSMENTS_FILE.open('r', encoding='utf-8') as sample_file:
                return json.load(sample_file)
        except json.JSONDecodeError:
            return []
    return []


def create_sample_assessments():
    sample_assessments = load_sample_assessments()
    if not sample_assessments:
        return
    for sample in sample_assessments:
        skill_data = sample['skill']
        skill, _ = Skill.objects.get_or_create(
            name=skill_data['name'],
            defaults={
                'category': skill_data['category'],
                'icon': skill_data['icon'],
            }
        )

        assessment, created = Assessment.objects.get_or_create(
            title=sample['title'],
            defaults={
                'skill': skill,
                'duration_minutes': sample['duration_minutes'],
                'total_marks': sample['total_marks'],
            }
        )
        if created:
            for question_data in sample['questions']:
                Question.objects.create(
                    assessment=assessment,
                    text=question_data['text'],
                    option_a=question_data['option_a'],
                    option_b=question_data['option_b'],
                    option_c=question_data['option_c'],
                    option_d=question_data['option_d'],
                    correct_option=question_data['correct_option'],
                    marks=question_data['marks'],
                )


@login_required
def assessment_list(request):
    create_sample_assessments()

    assessments = Assessment.objects.select_related('skill').all()
    categories = sorted({assessment.skill.category for assessment in assessments})
    track_count = len(categories)

    return render(request, 'assessments/list.html', {
        'assessments': assessments,
        'track_count': track_count,
        'categories': categories,
    })

@login_required
def take_assessment(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    questions = assessment.questions.all()

    if request.method == 'POST':
        score = 0
        total = 0
        for question in questions:
            selected = request.POST.get(f'q_{question.id}')
            total += question.marks
            if selected == question.correct_option:
                score += question.marks

        result = AssessmentResult(
            user=request.user,
            assessment=assessment,
            score=score
        )
        result.level = result.determine_level()
        result.save()

        return redirect('assessments:result', result_id=result.id)

    return render(request, 'assessments/take.html', {
        'assessment': assessment,
        'questions': questions,
    })

@login_required
def assessment_result(request, result_id):
    result = get_object_or_404(AssessmentResult, id=result_id, user=request.user)
    percentage = (result.score / result.assessment.total_marks) * 100
    return render(request, 'assessments/result.html', {
        'result': result,
        'percentage': round(percentage, 1),
    })
