from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFOD=StudentForm(request.POST)
        if SFOD.is_valid():
            return HttpResponse(str(SFOD.cleaned_data))
        else:
            return HttpResponse('data is not valid')
    return render(request,'student.html',d)