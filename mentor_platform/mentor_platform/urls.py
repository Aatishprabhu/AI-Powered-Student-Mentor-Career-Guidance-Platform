from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard import views as dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('assessments/', include('assessments.urls', namespace='assessments')),
    path('roadmaps/', include('roadmaps.urls', namespace='roadmaps')),
    path('mentor/', include('mentor.urls', namespace='mentor')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('placements/', include('placements.urls', namespace='placements')),
    path('analytics/', include('analytics.urls', namespace='analytics')),
    path('', dashboard_views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)