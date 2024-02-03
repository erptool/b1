from django.shortcuts import render, redirect
from .forms import TipForm, SearchForm
from django.http import HttpResponse
from .models import Tip
from django.db.models import Q
from django.views.generic import DetailView

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

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            results = Tip.objects.filter(title=search_text)
            return render(request, 'main/index.html', {'form': form, 'results': results})
    else:
        form = SearchForm()
    return render(request, 'main/index.html', {'form': form})

class ObjectDetailView(DetailView):
    model = Tip
    template_name = 'main/object_detail.html'
    context_object_name = 'object'

# Create your views here.
