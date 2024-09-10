from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView,CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_View(), name = 'login'),
    path('',TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('task_create/', TaskCreate.as_view(), name = 'task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name = 'task_update'),
    path('task_delete/<int:pk>/', DeleteView.as_view(), name = 'task_delete'),

]