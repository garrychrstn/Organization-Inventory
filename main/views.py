from django.shortcuts import render, get_object_or_404, redirect
from . forms import *
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def index(response):
    eves = Events.objects.all().order_by('-upt')[:1]

    return render(response, 'index.html', {'eves' : eves})

@login_required
def addEvent(response):
    if response.method == 'POST':
        form = FormEvent(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            date = form.cleaned_data['date']
            desc = form.cleaned_data['desc']
            img = form.cleaned_data['img']
            reg = form.cleaned_data['reg']
        
        e = Events(name=name, type=type, date=date, desc=desc, img=img, reg=reg)
        e.save()

        form = FormEvent()

        context = {
            'form' : form,
        }

        return render(response, 'adminAddEvent.html', context)
    else:
        form = FormEvent()
        return render(response, 'adminAddEvent.html', {'form' : form})
    
@login_required
def addItems(response):
    if response.method == 'POST':
        form = FormItems(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            penerima = form.cleaned_data['penerima']
            type = form.cleaned_data['type']
            amount = form.cleaned_data['amount']
            owner = form.cleaned_data['owner']
            dateIn = form.cleaned_data['dateIn']
            desc = form.cleaned_data['desc']
            location = form.cleaned_data['location']
        
        e = Goods(name=name, penerima=penerima, type=type, amount=amount, owner=owner, dateIn=dateIn, desc=desc, location=location)
        e.save()

        form = FormItems()

        context = {
            'form' : form,
        }

        return render(response, 'adminAddItems.html', context)
    else:
        form = FormItems()
        return render(response, 'adminAddItems.html', {'form' : form})

    
@login_required
def displayItems(response):
    goods = Goods.objects.all()
    context = {
        'goods' : goods,
    }

    return render(response, 'displayItem.html', context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged as {username}")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid Password or Username")
        else:
            messages.error(request, "Invalid Password or Username")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form' : form}) 

@login_required
def addMembers(response):
    if response.method == 'POST':
        form = FormMember(response.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            position = form.cleaned_data['position']
            year = form.cleaned_data['year']
            program = form.cleaned_data['program']
            potrait = form.cleaned_data['potrait']

        m = Members(name=name, position=position, year=year, program=program, potrait=potrait)
        m.save()

        form = FormMember()

        context = {
            'form' : form,
        }

        return render(response, 'adminAddItems.html', context)
    else:
        form = FormMember()
        return render(response, 'adminAddMembers.html', {'form' : form})

def displayMember(request):
    return render(request, 'displayMember.html')