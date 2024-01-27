from django.urls import path
from TaskApp.views import *
urlpatterns = [
    path('',TaskListView.as_view(),name='task_list'),
    path('task_create/',TaskCreateView.as_view(), name='task_create'),
    path('task_detail/<int:pk>/',TaskDetailView.as_view(), name= 'task_detail'),
    path('task_update/<int:pk>/',TaskUpdateView.as_view(), name= 'task_update'),
    path('task_delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete')
]
