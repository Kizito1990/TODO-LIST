from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.Views import LoginView
from .models import Tasks

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def success_url(self):
        return reverse_lazy('tasks')
class TaskList(ListView):
    model = Tasks
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'todolist/task.html'

class TaskCreate(CreateView):
    model = Tasks
    template_name = 'todolist/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Tasks
    template_name = 'todolist/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Tasks
    template_name = 'todolist/tasks_comfirm_delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')