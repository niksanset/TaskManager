from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView,DeleteView,UpdateView,CreateView
from TaskApp.models import *
from django.urls import reverse_lazy

class TaskListView(ListView):
    template_name = 'TaskApp/task_list.html'
    model = Task
    context_object_name = 'task_list'

class TaskCreateView(CreateView):
    template_name = 'TaskApp/task_create.html'
    model = Task
    fields = ('__all__')
    success_url = reverse_lazy('task_list')

class TaskDetailView(DetailView):
    template_name = 'TaskApp/task_detail.html'
    model = Task

class TaskUpdateView(UpdateView):
    template_name = 'TaskApp/task_update.html'
    model = Task
    fields = ('__all__')
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    tempalte_name = 'TaskApp/task_delete.html'
    model = Task
    fields = ('__all__')
    success_url = reverse_lazy('task_list')