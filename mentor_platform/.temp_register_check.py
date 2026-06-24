import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentor_platform.settings')
import django
django.setup()
from accounts.forms import RegisterForm

data = {
    'username': 'testuser2',
    'email': 'test2@example.com',
    'password1': 'Testpass123',
    'password2': 'Testpass123',
    'college': 'ABC University',
    'graduation_year': '2025',
}
form = RegisterForm(data)
print('is_valid:', form.is_valid())
print('errors:', form.errors)
print('non_field_errors:', form.non_field_errors())
