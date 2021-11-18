from django.shortcuts import render, redirect,get_object_or_404
from .models import item 
from .forms import AddItem
from .forms import UpdateItem

def index(request):
    items = item.objects.filter(item_user = request.user)
    if request.method =='POST':
        Date = request.POST["Filter_Date"]
        if Date == "":
            context ={
                'item_list': items,
            }
            return render(request, "index.html", context)

        Filtered_items = items.filter(item_date = Date)
        context ={
            'item_list': Filtered_items,
            'current_date': Date,
        }
        return render(request, "index.html", context)
    else:
        context ={
            'item_list': items,
        }
        return render(request, "index.html", context)

def add_item(request):
    if request.method=='POST':
        form= AddItem(request.POST, request.FILES)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.item_user = request.user
            instance.save()
            return redirect('index')
    else:
        form= AddItem()
    return render(request, 'add.html',{'form':form})

def updateitem(request, item_id):
    obj = get_object_or_404(item, pk=item_id)
    
    if request.method=='POST':
        form= UpdateItem(request.POST,instance=obj)
        
        if form.is_valid():
            instance= form.save(commit=False)
            if instance.item_user == request.user:
                instance.save()
            return redirect('index')
    else:
        form= UpdateItem(instance=obj)
    return render(request, 'update.html',{'form':form, 'obj':obj})

def deleteitem(request, item_id):
    obj = get_object_or_404(item, pk=item_id)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        obj.delete()                     # delete the cat.
        return redirect('index')       

    return render(request, 'delete.html', {'obj': obj})    

