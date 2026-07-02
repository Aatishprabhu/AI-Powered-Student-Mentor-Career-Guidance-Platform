# AI-Powered Student Mentor & Career Guidance Platform

A full-stack Django web application designed to help students improve their skills, track progress, prepare for interviews, explore career opportunities, and receive AI-assisted guidance.

This platform combines assessment-based learning, personalized roadmaps, project recommendations, placement tracking, and an AI mentor experience in a single dashboard.

## 🚀 Project Overview

The platform is built to support students throughout their learning and career journey by providing:

- Skill assessments and progress tracking
- Personalized learning roadmaps
- AI-powered mentor chat and resume feedback
- Recommended projects based on assessment performance
- Placement application tracking and status updates
- Analytics dashboards for learning and placement progress

## ✨ Key Features

### 1. User Authentication and Profiles
- Secure registration and login
- Custom user model with student/admin/mentor roles
- Profile details such as college, graduation year, LinkedIn, GitHub, and bio

### 2. Skill Assessment System
- Multiple skill-based assessments
- MCQ questions with scoring and result evaluation
- Automatic skill level classification (Beginner, Intermediate, Advanced)

### 3. Learning Roadmaps
- Personalized roadmap creation for different skills
- Weekly learning structure with topics and resources
- Progress tracking through completion percentage

### 4. AI Mentor Assistant
- AI-based chat assistant for student queries
- Resume analysis for job-specific feedback
- Interview answer evaluation support

### 5. Project Recommendations
- Suggested projects based on user skill levels and assessment history
- Project templates with skill requirements, estimated hours, and resources

### 6. Placement Tracking
- Add and manage placement applications
- Track status such as Applied, Interview, Offer, Rejected, or Withdrawn
- Keep notes and salary details for each application

### 7. Analytics Dashboard
- Visualize assessment performance
- Monitor skill-level trends over time
- View placement application statistics and recent performance history

## 🛠️ Tech Stack

- Python 3
- Django 6.0+
- SQLite (default database)
- PostgreSQL support via environment variables
- HTML, CSS, Bootstrap-style templates
- JavaScript for interactive UI behavior
- Google Generative AI integration
- PyPDF2 for resume parsing
- Pillow for image handling
- WhiteNoise for static file serving

## 📁 Project Structure

```text
mentor_platform/
├── accounts/              # Authentication, user profiles, and registration/login views
├── analytics/             # Progress and placement analytics views
├── assessments/           # Quiz assessments, questions, scoring, and results
├── dashboard/             # Main dashboard and user overview
├── mentor/                # AI mentor chat, resume analyzer, interview feedback
├── placements/            # Placement applications and tracking
├── projects/              # Project recommendations and templates
├── roadmaps/              # Learning roadmaps and weekly planning
├── static/                # CSS and static assets
├── templates/             # Shared HTML templates
├── mentor_platform/       # Django project settings, URLs, and WSGI/ASGI config
├── db.sqlite3             # Default database file
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## 🧩 Main Modules

### Accounts Module
Handles authentication and user management.

### Dashboard Module
Provides the homepage dashboard with recent assessments, placement applications, and roadmap progress.

### Assessments Module
Contains assessments, quiz questions, skill models, and result tracking.

### Mentor Module
Provides AI assistance through:
- chat-based support
- resume analysis
- interview answer evaluation

### Projects Module
Recommends learning projects based on user skill profile and assessment results.

### Placements Module
Helps students track job applications and their progress.

### Roadmaps Module
Creates structured learning roadmaps with weekly topics and resources.

### Analytics Module
Provides progress and performance insights for students.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Aatishprabhu/AI-Powered-Student-Mentor-Career-Guidance-Platform.git
cd AI-Powered-Student-Mentor-Career-Guidance-Platform
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
cd mentor_platform
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open your browser at:

```text
http://127.0.0.1:8000/
```

## 🗃️ Database Configuration

The project uses SQLite by default.

If you want to use PostgreSQL, set the following environment variables:

```bash
export DB_ENGINE=postgres
export DB_NAME=mentor_db
export DB_USER=postgres
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=5432
```

## 🧪 Sample Data

The application can generate sample assessments and project templates automatically through the view logic so that the platform has content to explore immediately after setup.

## 📌 Usage Guide

1. Register a new account or log in.
2. Visit the dashboard to see your progress overview.
3. Take assessments to evaluate your current skills.
4. Explore recommended projects based on your performance.
5. Track job applications in the placements section.
6. Use the mentor tools for career advice, resume review, and interview preparation.

## 🔒 Notes

- The project is currently configured for development use.
- Sensitive settings such as the Django secret key should be moved to environment variables in production.
- Static files and media uploads should be configured properly for deployment.

## 🤝 Contributing

Contributions are welcome. You can:

- Improve UI/UX
- Add more assessments and projects
- Extend AI features
- Improve analytics and recommendations


