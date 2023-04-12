from django.urls import path
from . import views

app_name = 'scheduler'

urlpatterns = [

    # scheduler/month/
    path('month/',views.month, name= 'month'),

    # scheduler/create/
    path('create/', views.create_schedule, name= 'create_schedule'),

    # scheduler/
    path('', views.index_schedule, name='index_schedule'),

    # scheduler/1/
    path('<int:schedule_pk>/', views.detail_schedule, name='detail_schedule'),

    # scheduler/1/update/
    path('<int:schedule_pk>/update/', views.update_schedule, name='update_schedule'),

    # scheduler/1/delete/
    path('<int:schedule_pk>/delete/', views.delete_schedule, name='delete_schedule'),





]