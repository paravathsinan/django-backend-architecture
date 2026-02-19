from django.shortcuts import render, redirect, get_object_or_404
from .models import Worker
from .forms import WorkerForm


def worker_list(request):
    
    workers = Worker.objects.all()
    workers = Worker.objects.order_by("name")
    
    context = {
        "workers":workers,
        } 
    return render(request, "workers/workers.html", context)


def add_worker(request):
    form = WorkerForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/workers/')
    
    return render(request, 'workers/crud_worker.html', {"form":form})


def edit_worker(request,id):
    worker = get_object_or_404(Worker, id=id)
    form = WorkerForm(request.POST or None, instance=worker)
    
    if form.is_valid():
        form.save()
        
        return redirect('/workers/')
    
    return render(request, 'workers/crud_worker.html', {'form':form})


def delete_worker(request, id):
    worker = get_object_or_404(Worker, id=id)
    worker.delete()
    return redirect('/workers/')







