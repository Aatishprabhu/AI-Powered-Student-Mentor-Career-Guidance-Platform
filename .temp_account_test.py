import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mentor_platform.settings')
import django
django.setup()
from django.test import Client
from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.filter(username='testuser').delete()
client = Client()
print('register GET', client.get('/accounts/register/').status_code)
print('login GET', client.get('/accounts/login/').status_code)
resp = client.post('/accounts/register/', {
    'username': 'testuser',
    'email': 'testuser@example.com',
    'password1': 'Testpass123',
    'password2': 'Testpass123',
})
print('register POST', resp.status_code, getattr(resp, 'url', None))
resp2 = client.post('/accounts/login/', {
    'username': 'testuser',
    'password': 'Testpass123',
})
print('login POST', resp2.status_code, getattr(resp2, 'url', None))
print('authenticated', resp2.wsgi_request.user.is_authenticated)
