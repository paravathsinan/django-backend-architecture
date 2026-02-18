from django.shortcuts import render ,redirect
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





