from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tasks

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def success_url(self):
        return reverse_lazy('tasks')
class TaskList(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = 'tasks'

    def get_data_context(self, **kwargs):
        user = self.request.user
        return Tasks.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.get_data_context()
        user = self.request.user

        # Get tasks specific to the logged-in user
        user_tasks = Tasks.objects.filter(user=user)

        # Count completed and uncompleted tasks
        completed_count = user_tasks.filter(complete=True).count()
        uncompleted_count = user_tasks.filter(complete=False).count()

        context['user_tasks'] = user_tasks
        context['completed_count'] = completed_count
        context['uncompleted_count'] = uncompleted_count
        return context



class TaskDetail(LoginRequiredMixin, DetailView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'todolist/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'todolist/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'todolist/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'todolist/tasks_comfirm_delete.html'
    context_object_name = 'tasks'
    success_url = reverse_lazy('tasks')