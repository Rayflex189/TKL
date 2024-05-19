from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    return render(request, 'T_K_L/index.html')

def details(request):
    form = Details.objects.all()
    context = {'form':form}
    return render(request, 'T_K_L/details.html', context)