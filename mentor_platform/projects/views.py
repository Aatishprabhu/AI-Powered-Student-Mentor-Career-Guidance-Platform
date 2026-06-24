from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assessments.models import AssessmentResult, Skill
from .models import Project
import json

LEVEL_PRIORITY = {'beginner': 1, 'intermediate': 2, 'advanced': 3}

PROJECT_TEMPLATES = [
    {
        'title': 'Python Portfolio Website',
        'description': 'Build a portfolio site with dynamic content, project showcases, and contact form using Python and Django.',
        'skills': ['Python'],
        'categories': ['Programming'],
        'level': 'beginner',
        'estimated_hours': 10,
        'github_template': 'https://github.com/topics/portfolio-website?l=python',
        'resources': [
            'https://github.com/topics/portfolio-website?l=python',
            'https://docs.djangoproject.com/en/stable/intro/tutorial01/',
            'https://getbootstrap.com/docs/5.0/getting-started/introduction/'
        ],
    },
    {
        'title': 'Data Structures Visualizer',
        'description': 'Create an app that visualizes arrays, stacks, queues and linked lists with interactive controls.',
        'skills': ['Data Structures'],
        'categories': ['Computer Science'],
        'level': 'intermediate',
        'estimated_hours': 18,
        'github_template': 'https://github.com/trekhleb/javascript-algorithms',
        'resources': [
            'https://visualgo.net/en',
            'https://www.geeksforgeeks.org/data-structures/',
            'https://www.freecodecamp.org/news/data-structures-for-beginners/'
        ],
    },
    {
        'title': 'Interview Prep Tracker',
        'description': 'Build a project tracking dashboard for interview questions, practice sessions, and improvement goals.',
        'skills': ['Career Skills', 'Python'],
        'categories': ['Professional Development'],
        'level': 'beginner',
        'estimated_hours': 12,
        'github_template': 'https://github.com/Nikitha2309/Interview-Prep-Tracker-Website',
        'resources': [
            'https://github.com/Nikitha2309/Interview-Prep-Tracker-Website',
            'https://www.pramp.com/',
            'https://leetcode.com/'
        ],
    },
    {
        'title': 'Skill-Based Job Match Dashboard',
        'description': 'Develop a dashboard that recommends roles and projects based on a user’s skill profile and assessment results.',
        'skills': ['Data Structures', 'Python'],
        'categories': ['Computer Science', 'Programming'],
        'level': 'advanced',
        'estimated_hours': 25,
        'github_template': 'https://github.com/nikhilkumarsingh/django-dashboard',
        'resources': [
            'https://realpython.com/django-admin-customization/',
            'https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django',
            'https://developer.mozilla.org/en-US/docs/Web/JavaScript'
        ],
    },
    {
        'title': 'Career Growth Planner',
        'description': 'Create a planning tool that tracks goals, timelines, and skill milestones for career development.',
        'skills': ['Career Skills'],
        'categories': ['Professional Development'],
        'level': 'intermediate',
        'estimated_hours': 16,
        'github_template': 'https://github.com/andrewjfreyer/career-tracker',
        'resources': [
            'https://github.com/topics/career-path',
            'https://www.themuse.com/advice/career-development',
            'https://www.linkedin.com/learning/'
        ],
    },
    {
        'title': 'Microlearning Flashcards App',
        'description': 'Build a flashcard study tool with spaced repetition, progress tracking, and quiz review features.',
        'skills': ['Python'],
        'categories': ['Education', 'Programming'],
        'level': 'beginner',
        'estimated_hours': 14,
        'github_template': 'https://github.com/topics/flashcard-app?l=python',
        'resources': [
            'https://en.wikipedia.org/wiki/Spaced_repetition',
            'https://realpython.com/django-forms/,',
            'https://www.chartjs.org/'
        ],
    },
    {
        'title': 'Smart Study Session Planner',
        'description': 'Create an intelligent study planner that schedules sessions, breaks, and task priorities by topic.',
        'skills': ['Python', 'Career Skills'],
        'categories': ['Productivity', 'Programming'],
        'level': 'intermediate',
        'estimated_hours': 18,
        'github_template': 'https://github.com/topics/study-planner?l=python',
        'resources': [
            'https://github.com/topics/study-planner?l=python',
            'https://realpython.com/python-datetime/',
            'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date'
        ],
    },
    {
        'title': 'Open-Source Contribution Tracker',
        'description': 'Build a dashboard that tracks GitHub contributions, issue progress, and open source badges.',
        'skills': ['Python', 'Data Structures'],
        'categories': ['Community', 'Programming'],
        'level': 'intermediate',
        'estimated_hours': 22,
        'github_template': 'https://github.com/topics/contribution-tracker?l=python',
        'resources': [
            'https://docs.github.com/en/rest',
            'https://opensource.guide/how-to-contribute/',
            'https://realpython.com/python-requests/'
        ],
    },
    {
        'title': 'Budget & Expense Manager',
        'description': 'Create a personal finance app with expense categories, savings goals, and analytics summaries.',
        'skills': ['Python', 'Data Structures'],
        'categories': ['Finance', 'Programming'],
        'level': 'beginner',
        'estimated_hours': 16,
        'github_template': 'https://github.com/topics/expense-tracker?l=python',
        'resources': [
            'https://www.investopedia.com/personal-finance-4427767',
            'https://realpython.com/python-matplotlib-guide/',
            'https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django'
        ],
    },
]


def create_sample_projects():
    for template in PROJECT_TEMPLATES:
        skills = []
        for skill_name in template['skills']:
            skill, _ = Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    'category': template.get('categories', ['General'])[0],
                    'icon': skill_name[:2].upper(),
                }
            )
            skills.append(skill)

        project, created = Project.objects.get_or_create(
            title=template['title'],
            defaults={
                'description': template['description'],
                'level': template['level'],
                'estimated_hours': template['estimated_hours'],
                'github_template': template['github_template'],
                'resources': json.dumps(template['resources']),
            }
        )
        if created:
            project.skills_required.set(skills)
            project.save()


@login_required
def recommended_projects(request):
    create_sample_projects()

    user = request.user
    user_results = (
        AssessmentResult.objects.filter(user=user)
        .select_related('assessment__skill')
        .order_by('assessment__skill', '-completed_at')
    )

    user_skill_levels = {}
    for result in user_results:
        skill = result.assessment.skill
        existing = user_skill_levels.get(skill)
        if not existing or LEVEL_PRIORITY[result.level] > LEVEL_PRIORITY[existing]:
            user_skill_levels[skill] = result.level

    all_projects = Project.objects.prefetch_related('skills_required').all()
    recommended = []

    if user_skill_levels:
        for project in all_projects:
            project_skill_names = {skill.name for skill in project.skills_required.all()}
            skill_match = False
            for skill, level in user_skill_levels.items():
                if skill.name in project_skill_names and LEVEL_PRIORITY[project.level] <= LEVEL_PRIORITY[level]:
                    skill_match = True
                    break
            if skill_match:
                recommended.append(project)

        if len(recommended) < 6:
            beginner_fallback = [
                project for project in all_projects
                if project.level == 'beginner' and project not in recommended
            ]
            for project in beginner_fallback:
                if len(recommended) >= 6:
                    break
                recommended.append(project)
    else:
        recommended = all_projects.filter(level='beginner')

    recommended = sorted(recommended, key=lambda p: (LEVEL_PRIORITY[p.level], p.estimated_hours))

    for project in recommended:
        try:
            project.resources_list = json.loads(project.resources or '[]')
        except json.JSONDecodeError:
            project.resources_list = []

    return render(request, 'projects/list.html', {
        'projects': recommended,
        'user_skills': user_skill_levels,
        'has_results': bool(user_skill_levels),
    })
