from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from datetime import datetime
from django.utils.dateformat import DateFormat

from .models import Schedule
from .forms import ScheduleForm





def month(request,):
    schedules = Schedule.objects.all()

    daily_schedules_01 = Schedule.objects.filter(date = '2023-04-01')
    daily_schedules_02 = Schedule.objects.filter(date = '2023-04-02')
    daily_schedules_03 = Schedule.objects.filter(date = '2023-04-03')
    daily_schedules_04 = Schedule.objects.filter(date = '2023-04-04')
    daily_schedules_05 = Schedule.objects.filter(date = '2023-04-05')
    daily_schedules_06 = Schedule.objects.filter(date = '2023-04-06')
    daily_schedules_07 = Schedule.objects.filter(date = '2023-04-07')
    daily_schedules_08 = Schedule.objects.filter(date = '2023-04-08')
    daily_schedules_09 = Schedule.objects.filter(date = '2023-04-09')
    daily_schedules_10 = Schedule.objects.filter(date = '2023-04-10')
    daily_schedules_11 = Schedule.objects.filter(date = '2023-04-11')
    daily_schedules_12 = Schedule.objects.filter(date = '2023-04-12')
    daily_schedules_13 = Schedule.objects.filter(date = '2023-04-13')
    daily_schedules_14 = Schedule.objects.filter(date = '2023-04-14')
    daily_schedules_15 = Schedule.objects.filter(date = '2023-04-15')
    daily_schedules_16 = Schedule.objects.filter(date = '2023-04-16')
    daily_schedules_17 = Schedule.objects.filter(date = '2023-04-17')
    daily_schedules_18 = Schedule.objects.filter(date = '2023-04-18')
    daily_schedules_19 = Schedule.objects.filter(date = '2023-04-19')
    daily_schedules_20 = Schedule.objects.filter(date = '2023-04-20')
    daily_schedules_21 = Schedule.objects.filter(date = '2023-04-21')
    daily_schedules_22 = Schedule.objects.filter(date = '2023-04-22')
    daily_schedules_23 = Schedule.objects.filter(date = '2023-04-23')
    daily_schedules_24 = Schedule.objects.filter(date = '2023-04-24')
    daily_schedules_25 = Schedule.objects.filter(date = '2023-04-25')
    daily_schedules_26 = Schedule.objects.filter(date = '2023-04-26')
    daily_schedules_27 = Schedule.objects.filter(date = '2023-04-27')
    daily_schedules_28 = Schedule.objects.filter(date = '2023-04-28')
    daily_schedules_29 = Schedule.objects.filter(date = '2023-04-29')
    daily_schedules_30 = Schedule.objects.filter(date = '2023-04-30')
    


    return render(request, 'scheduler/month.html', 
                  {'schedules': schedules,
                   'daily_schedules_01':daily_schedules_01,
                   'daily_schedules_02':daily_schedules_02,
                   'daily_schedules_03':daily_schedules_03,
                   'daily_schedules_04':daily_schedules_04,
                   'daily_schedules_05':daily_schedules_05,
                   'daily_schedules_06':daily_schedules_06,
                   'daily_schedules_07':daily_schedules_07,
                   'daily_schedules_08':daily_schedules_08,
                   'daily_schedules_09':daily_schedules_09,
                   'daily_schedules_10':daily_schedules_10,
                   'daily_schedules_11':daily_schedules_11,
                   'daily_schedules_12':daily_schedules_12,
                   'daily_schedules_13':daily_schedules_13,
                   'daily_schedules_14':daily_schedules_14,
                   'daily_schedules_15':daily_schedules_15,
                   'daily_schedules_16':daily_schedules_16,
                   'daily_schedules_18':daily_schedules_18,
                   'daily_schedules_17':daily_schedules_17,
                   'daily_schedules_19':daily_schedules_19,
                   'daily_schedules_20':daily_schedules_20,
                   'daily_schedules_21':daily_schedules_21,
                   'daily_schedules_22':daily_schedules_22,
                   'daily_schedules_23':daily_schedules_23,
                   'daily_schedules_24':daily_schedules_24,
                   'daily_schedules_25':daily_schedules_25,
                   'daily_schedules_26':daily_schedules_26,
                   'daily_schedules_27':daily_schedules_27,
                   'daily_schedules_28':daily_schedules_28,
                   'daily_schedules_29':daily_schedules_29,
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
    today = DateFormat(datetime.now()).format('Y-m-d')
    today_schedules = Schedule.objects.filter(date = today)

    return render(request, 'scheduler/index.html', {'schedules': schedules,
                                                    
                                                    'today_schedules':today_schedules,})
    


def detail_schedule(request, schedule_pk):
    schedule = get_object_or_404(Schedule, pk = schedule_pk)

    return render(request, 'scheduler/detail.html', {'schedule': schedule})
   

@login_required
@require_http_methods(['GET', 'POST'])
def update_schedule(request, schedule_pk):

    schedule = get_object_or_404(Schedule, pk = schedule_pk)

    if request.user != schedule.user:
        return redirect('scheduler:detail_schedule', schedule.pk)

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

    if request.user != schedule.user:
        return redirect('scheduler:detail_schedule', schedule.pk)
    
    schedule.delete()
    return redirect('scheduler:index_schedule')

