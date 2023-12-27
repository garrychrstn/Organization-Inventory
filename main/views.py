from django.shortcuts import render
from . forms import *
from . models import *
# Create your views here.
def index(response):
    eves = Events.objects.all().order_by('-upt')[:1]

    return render(response, 'index.html', {'eves' : eves})

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
    