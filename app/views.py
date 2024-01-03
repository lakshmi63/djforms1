from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *


def djforms(request):
    SFDO=SchoolForm()
    d={'SFDO': SFDO}
    if request.method=='POST':
        SFO=SchoolForm(request.POST)
        if SFO.is_valid():
            sn=SFO.cleaned_data['Sname']
            sp=SFO.cleaned_data['Sprincipal']
            sl=SFO.cleaned_data['Slocation']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sl)[0]
            SO.save()
            return HttpResponse('school is created')
        else:
            return HttpResponse('invalid data')

    
    return render(request,'djforms.html',d)
