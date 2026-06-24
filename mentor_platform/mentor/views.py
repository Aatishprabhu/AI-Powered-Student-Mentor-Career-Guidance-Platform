from django.shortcuts import render
 
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import MentorChat
from .ai_utils import get_chat_response, get_gemini_response

@login_required
def mentor_chat_view(request):
    chats = MentorChat.objects.filter(user=request.user).order_by('created_at')[:20]
    return render(request, 'mentor/chat.html', {'chats': chats})

@login_required
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        
        past_chats = MentorChat.objects.filter(user=request.user).order_by('-created_at')[:5]
        history = []
        for chat in reversed(past_chats):
            history.append({"role": "user", "parts": [chat.message]})
            history.append({"role": "model", "parts": [chat.response]})

        
        user = request.user
        context_prompt = f"""
        Student Profile:
        - Name: {user.get_full_name() or user.username}
        - College: {user.college}
        - Graduation Year: {user.graduation_year}

        Student's question: {user_message}
        """

        ai_response = get_chat_response(history, context_prompt)

        
        MentorChat.objects.create(
            user=request.user,
            message=user_message,
            response=ai_response
        )

        return JsonResponse({'response': ai_response, 'status': 'ok'})
    return JsonResponse({'error': 'Invalid method'}, status=405)



from .resume_utils import analyze_resume

@login_required
def resume_analyzer_view(request):
    analysis = None
    if request.method == 'POST' and request.FILES.get('resume'):
        pdf_file = request.FILES['resume']
        target_role = request.POST.get('target_role', 'Software Engineer')
        analysis = analyze_resume(pdf_file, target_role)
    return render(request, 'mentor/resume.html', {'analysis': analysis})     


@login_required
@csrf_exempt
def evaluate_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question_id = data.get('question_id')
        user_answer = data.get('answer', '')

        from .models import InterviewQuestion, InterviewPractice
        question = InterviewQuestion.objects.get(id=question_id)

        prompt = f"""
        Interview Question: {question.question}
        Domain: {question.domain}
        Difficulty: {question.difficulty}

        Student's Answer: {user_answer}

        Please evaluate this answer and provide:
        1. Score (1-10)
        2. What was good about this answer
        3. What was missing or incorrect
        4. A better/model answer
        5. Tips for next time

        Be encouraging but honest.
        """

        feedback = get_gemini_response(prompt)

        
        score = 5
        for line in feedback.split('\n'):
            if 'score' in line.lower() and any(char.isdigit() for char in line):
                digits = [int(c) for c in line if c.isdigit()]
                if digits:
                    score = min(digits[0], 10)
                    break

        InterviewPractice.objects.create(
            user=request.user,
            question=question,
            user_answer=user_answer,
            ai_feedback=feedback,
            ai_score=score
        )

        return JsonResponse({'feedback': feedback, 'score': score})
    return JsonResponse({'error': 'Invalid'}, status=400)
