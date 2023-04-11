from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Schedule
from .forms import ScheduleForm

def create_schedule(request):
    if request.method == 'GET':
        form = ScheduleForm()

    else:
        form = ScheduleForm(request.POST)
        if form.is_valid:
            schedule = form.save()
            return redirect('scheduler:detail_schedule', schedule.pk)
        
    return render(request, 'scheduler/create.html', {'form': form})



def index_schedule(request):
    schedules = Schedule.objects.all()

    return render(request, 'Scheduler/index.html', {'schedules': schedules,})
    


def detail_schedule(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk = schedule_pk)

    return render(request, 'scheduler/detail.html', {'schedule': schedule})
   


def update_schedule(request, schedule_pk):

    schedule = get_object_or_404(Schedule, pk = schedule_pk)

    if request.method == 'GET':
        form = ScheduleForm(instance=schedule)
        
    elif request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            schedule = form.save()

            return redirect('scheduler:detail_schedule', schedule.pk)

    return render(request, 'scheduler/update.html', {
        'form': form,
    })


def delete_schedule(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk = schedule_pk)
    schedule.delete()
    return redirect('scheduler:index_schedule')