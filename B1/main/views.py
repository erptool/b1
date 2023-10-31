from django.shortcuts import render, redirect
from .forms import TipForm
from django.http import HttpResponse
from .models import Tip

def index(request):
     objects = Tip.objects.all()
     return render(request, 'main/index.html', {'objects': objects})


def TipView(request):
    objects = Tip.objects.all()
    if request.method == 'POST':
        form = TipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Save the form data to the database
            return render(request, 'main/index.html', {'objects': objects})
    else:
        form = TipForm()
    return render(request, 'main/home.html', {'form': form})    




# Create your views here.
