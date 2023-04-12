from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from .models import Schedule
from .forms import ScheduleForm




def month(request,):
    schedules = Schedule.objects.all()

    daily_schedules_03 = Schedule.objects.filter(date = '2023-04-03')
    
    daily_schedules_12 = Schedule.objects.filter(date = '2023-04-12')
    
    daily_schedules_14 = Schedule.objects.filter(date = '2023-04-14')
    daily_schedules_30 = Schedule.objects.filter(date = '2023-04-30')
    


    return render(request, 'scheduler/month.html', 
                  {'schedules': schedules,
                   'daily_schedules_03':daily_schedules_03,
                   'daily_schedules_12':daily_schedules_12,
                   'daily_schedules_14':daily_schedules_14,
                   'daily_schedules_30':daily_schedules_30,
                   
                   })

@login_required
@require_http_methods(['GET', 'POST'])
def create_schedule(request):
    if request.method == 'GET':
        form = ScheduleForm()
        return render(request, 'scheduler/create.html', {'form': form})

    else:
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('scheduler:detail_schedule', schedule.pk)
        


def index_schedule(request):
    schedules = Schedule.objects.all()

    return render(request, 'scheduler/index.html', {'schedules': schedules,})
    


def detail_schedule(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk = schedule_pk)

    return render(request, 'scheduler/detail.html', {'schedule': schedule})
   

@login_required
@require_http_methods(['GET', 'POST'])
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
        'form': form, 'schedule': schedule,
    })


@login_required
@require_POST
def delete_schedule(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk = schedule_pk)
    schedule.delete()
    return redirect('scheduler:index_schedule')

