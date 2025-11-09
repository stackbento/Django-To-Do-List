from django.shortcuts import render
from . models import List
from . forms import ListForm

# Create your views here.
def home(request):
    #access the objects in the List(from models.py/Database)
    all_items = List.objects.all()
    #convention : context dictionary to access the objects from 'all_items'
    context = {'all_items':all_items}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})