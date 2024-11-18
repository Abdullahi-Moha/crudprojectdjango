from django.shortcuts import render, redirect, get_object_or_404
from .models import item
# Create your views here.

#CRUD
#create
def create_item(request):
    if request.method == 'POST':
        name = request.POST.get['name']
        description= request.POST.get['description']
        item.objects.create(name=name, description=description)
        return redirect('item_list')
    return render(request, 'item_form.html')
#read
def read_item(request):
    items = item.objects.all()
    return render (request, 'item_form.html', {'items': items})

def update_item(request, pk):
  item=get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.name = request.POST.get['name']
        item.description = request.POST.get['description']
        item.save()
        return redirect('item_list')
    return render(request, 'item_form.html', {'item': item})
 #delete
 def delete_item(request, pk):
     item=get_object_or_404(item,pk=pk)
     if request.method == 'POST':
         item.delete()
         return redirect('item_list')
     return render(request, 'item_form.html', {'item': item})
