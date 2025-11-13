from django.shortcuts import render, redirect
from . models import List
from . forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method =='POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items=List.objects.all()
            messages.success(request, ('Item has been added to List!'))
            return redirect('home')
    else:        
        #access the objects in the List(from models.py/Database)
        all_items = List.objects.all()
        #convention : context dictionary to access the objects from 'all_items'
        context = {'all_items':all_items}
        return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')



#unfinished items
def incomplete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.is_completed=True
    item.save()
    return redirect('home')

#finished items
def complete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.is_completed=False
    item.save()
    return redirect('home')