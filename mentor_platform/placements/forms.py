from django import forms
from .models import PlacementApplication
import datetime

class ApplicationForm(forms.ModelForm):
    applied_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'max': datetime.date.today().isoformat(),
        }),
        initial=datetime.date.today,
    )
    
    class Meta:
        model = PlacementApplication
        fields = [
            'company_name',
            'role',
            'job_link',
            'applied_date',
            'status',
            'salary_offered',
            'notes',
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={
                'placeholder': 'e.g., Google, Microsoft, Amazon',
                'class': 'form-control',
            }),
            'role': forms.TextInput(attrs={
                'placeholder': 'e.g., Software Engineer, Data Analyst',
                'class': 'form-control',
            }),
            'job_link': forms.URLInput(attrs={
                'placeholder': 'https://example.com/job',
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
            'salary_offered': forms.TextInput(attrs={
                'placeholder': 'e.g., $80,000 - $100,000 per year',
                'class': 'form-control',
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Interview feedback, follow-up notes, etc.',
                'rows': 4,
                'class': 'form-control',
            }),
        }
