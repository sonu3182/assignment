from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("hii i am sonu kumar")
    return render(request,'index.html')

def car1(request):
    a=int(request.POST['num1'])
    if a>250:
        b=a-250
        c='Please remove weight in KG is'
        return render(request,'car1.html',{'result':b,'value':c})
    if a<250:
        b=250-a
        c='you can add weight in KG is'
        return render(request,'car1.html',{'result1':b,'value1':c})

def car2(request):
    a=int(request.POST['num1'])
    if a>250:
        b=a-250
        c='Please remove weight in KG is'
        return render(request,'car1.html',{'result':b,'value':c})
    if a<250:
        b=250-a
        c='you can add weight in KG is'
        return render(request,'car1.html',{'result1':b,'value1':c})


def car3(request):
    a=int(request.POST['num1'])
    if a>250:
        b=a-250
        c='Please remove weight in KG is'
        return render(request,'car1.html',{'result':b,'value':c})
    if a<250:
        b=250-a
        c='you can add weight in KG is'
        return render(request,'car1.html',{'result1':b,'value1':c})
