from django.shortcuts import get_object_or_404, render, redirect
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
    query = request.GET.get('search', '')
    results = []

    if query:
        results = Tip.search(query)

    context = {'results': results, 'query': query}
    return render(request, 'main/search_results.html', context)

def detail_view(request, pk):
    obj = get_object_or_404(Tip, pk=pk)
    return render(request, 'main/object_detail.html', {'obj': obj})

class ObjectDetailView(DetailView):
    model = Tip
    template_name = 'main/object_detail.html'
    context_object_name = 'object'

# Create your views here.
