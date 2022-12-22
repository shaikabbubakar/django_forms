from django.shortcuts import render
from app.forms import *
# Create your views here.

def django_forms(request):
    form=NameForm()
    d={'form':form}
    if request.method=='POST':
        Form_data=NameForm(request.POST)
        if Form_data.is_valid():
            name=Form_data.cleaned_data['name']
            age=Form_data.cleaned_data['age']
            password=Form_data.cleaned_data['password']
            email=Form_data.cleaned_data['email']
            gender=Form_data.cleaned_data['gender']
            courses=Form_data.cleaned_data['courses']
            address=Form_data.cleaned_data['address']
            d1={'n':name,'a':age,'p':password,'e':email,'g':gender,'c':courses,'ad':address}
            return render(request,'form_data.html',d1)
    return render(request,'django_forms.html',d)