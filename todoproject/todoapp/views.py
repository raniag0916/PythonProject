from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.models import Task
from todoapp.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
# CLASS BASED*********************************************

class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['task_Name', 'task_priority', 'task_Date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# FUNCTION BASED******************************************

def add(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        Name = request.POST.get('tname', '')
        Priority = request.POST.get('tpriority', '')
        Date = request.POST.get('tdate', '')
        task = Task(task_Name=Name, task_priority=Priority, task_Date=Date)
        task.save()
    return render(request, 'home.html', {'task1': task1})


# def details(request):
#     task1 = Task.objects.all()
#     return render(request, 'detail.html', {'task1': task1})

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})
