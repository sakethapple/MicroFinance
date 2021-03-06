from django.shortcuts import render
from .models import State,City,Customer,Agent,Investor,Suggetion,Loan_Scheme,Investment_scheme
from django.http import HttpResponse
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

def openAgentLogin(request):
    type =request.GET.get("type")
    return render(request,"index.html",{"type": type})

def openCustomerRegister (request) :
    type = request.GET.get("type")
    res=State.objects.values('state')
    states = ["Select"]
    for x in res:
        states.append(x["state"])
    return render(request, "index.html", {"type":type,"states":states})

def openInvestorRegister (request) :
    type = request.GET.get("type")
    res=State.objects.values('state')
    states = ["Select"]
    for x in res:
        states.append(x["state"])
    return render(request, "index.html", {"type":type,"states":states})

def getCityFromState(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('Id').filter(state=sel_state)
    idno = 0
    for x in res:
     idno = x["Id"]
    res1 = City.objects.values('city').filter(state_name=idno)

    city_name = ['City']
    if not res1:
        city_name = ["No city available"]
    else:
        for x in res1:
            city_name.append(x["city"])

    res2 = State.objects.values('state')
    states = ["State"]
    for x in res2:
       states.append(x["state"])

    return render(request,"index.html",{"type": 'h_customer_Register', "city_name": city_name, "states": sel_state, "key": "one"})

def getCityFromStateinvestor(request):
    sel_state = request.GET.get("state")
    res = State.objects.values('Id').filter(state=sel_state)
    idno = 0
    for x in res:
     idno = x["Id"]
    res1 = City.objects.values('city').filter(state_name=idno)

    city_name = ['City']
    if not res1:
        city_name = ["No city available"]
    else:
        for x in res1:
            city_name.append(x["city"])

    res2 = State.objects.values('state')
    states = ["State"]
    for x in res2:
       states.append(x["state"])

    return render(request,"index.html",{"type":'h_investor_Register', "city_name": city_name, "states": sel_state, "key": "two"})

def registercustomer(request):
    c_name=request.POST.get('c_name')
    c_contact = request.POST.get('c_contact')
    c_email = request.POST.get('c_email')
    c_password = request.POST.get('c_password')
    c_state = request.POST.get('c_state')
    c_city = request.POST.get('c_city')

    res=City.objects.values('Id').filter(city=c_city)
    idno=0
    for x in res:
        idno=x["Id"]
    cr=Customer(Name=c_name,city=City.objects.get(Id=idno),Email_id=c_email,contact_number=c_contact,password=c_password)
    cr.save()
    return render(request,"index.html",{"type":"h.customer","message":"Registred"})

def registerinvestor(request):
    I_name=request.POST.get('I_name')
    I_contact = request.POST.get('I_contact')
    I_email = request.POST.get('I_email')
    I_password = request.POST.get('I_password')
    I_state = request.POST.get('I_state')
    I_city = request.POST.get('I_city')

    res=City.objects.values('Id').filter(city=I_city)
    idno=0
    for x in res:
        idno=x["Id"]

    ir=Investor(Name=I_name,city=City.objects.get(Id=idno),Email_id=I_email,contact_number=I_contact,password=I_password)
    ir.save()
    return render(request,"index.html",{"type":"h.investor","message":"Registred"})

def openAgentRegister (request) :
    type = request.GET.get("type")
    return render(request, "index.html",{"type": type})

def registeragent(request):
    a_empid = request.POST.get('a_empid')
    a_name=request.POST.get('a_name')
    a_contact = request.POST.get('a_contact')
    a_email = request.POST.get('a_email')
    a_password = request.POST.get('a_password')


    print(a_name, a_contact, a_email, a_password, a_empid)

    ar=Agent(emp_id=a_empid,Name=a_name,contact_number=a_contact, Email_id=a_email,password=a_password)
    ar.save()
    return render(request,"index.html",{"type":'h.agent',"message":"Registred"})

def customerlogin(request):
    email = request.POST.get("c_name")
    password = request.POST.get("c_pass")

    res=Customer.objects.filter(Email_id=email,password=password)
    print(res)
    if not res:
        return render(request,"index.html",{"type":"h.customer","message":"Invalid login details" })
    else:
        for x in res:
            name=x
        return render(request,"customerhomepage.html",{"type":"customerhomepage","name":name})

def investorlogin(request):
    email=request.POST.get("i_name")
    password=request.POST.get("i_pass")
    res=Investor.objects.filter(Email_id=email,password=password)

    if not res:
        return render(request,'index.html',{"type":"h.investor","message":"Invalid Login Details"})
    else:
        for x in res:
         name=x
        return render(request,"investorhomepage.html",{"type":"investorhomepage","name":name})

def agentlogin(request):
    email=request.POST.get("a_name")
    password=request.POST.get("a_pass")
    res=Agent.objects.filter(Email_id=email,password=password)

    if not res:
        return render(request,"index.html",{"type":"h.agent","message":"Invalid Login Details"})
    else:
        for x in res:
            name=x
        return render(request,"agenthomepage.html",{"type":"agenthomepage","name":name})

def openloanpage(request):
    type=request.GET.get("type")
    res=Loan_Scheme.objects.all()
    for x in res:
        scheme=x
    return render(request,"customerhomepage.html",{"type":type,"scheme":scheme})