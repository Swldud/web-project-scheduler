from django.shortcuts import render

# Create your views here.

def month(request):

    return render(request, 'ephemeris/month.html')

