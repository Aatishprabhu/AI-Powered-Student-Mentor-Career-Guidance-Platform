from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PlacementApplication
from .forms import ApplicationForm

@login_required
def application_list(request):
    apps = PlacementApplication.objects.filter(user=request.user).order_by('-applied_date')
    stats = {
        'total': apps.count(),
        'interview': apps.filter(status='interview').count(),
        'offer': apps.filter(status='offer').count(),
        'rejected': apps.filter(status='rejected').count(),
    }
    return render(request, 'placements/list.html', {'applications': apps, 'stats': stats})

@login_required
def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.user = request.user
            app.save()
            return redirect('placements:list')
    else:
        form = ApplicationForm()
    return render(request, 'placements/add.html', {'form': form})

@login_required
def update_status(request, app_id):
    app = get_object_or_404(PlacementApplication, id=app_id, user=request.user)
    if request.method == 'POST':
        app.status = request.POST.get('status')
        app.notes = request.POST.get('notes', app.notes)
        app.save()
        return redirect('placements:list')
    return render(request, 'placements/update.html', {'app': app})
