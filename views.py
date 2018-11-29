from django.shortcuts import render
from .models import State,City
# Create your views here.

def openHomePage(request):
    type='home'
    return render(request,"index.html",{"type": type})

def openCustomerLogin(request):
    type =request.GET.get("type")
    return render(request,"index.html",{"type": type})

def openInvestorLogin(request):
    type =request.GET.get("type")
    return render(request,"index.html",{"type": type})

def openCustomerRegister(request):
    type=request.GET.get("type")
    res=State.objects.values('state')
    states=["select"]
    for x in res:
        states.append(x["state"])

    return render(request,"index.html",{"type":type,"states":states})

def getCityFromState(request):
    sel_state = request.GET.get("state")
    #res = State.objects.values('Id').filter(state=sel_state)

    res = City.objects.filter(state_name=sel_state)
    print(res)
    return None
