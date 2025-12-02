from django.urls import path, include
from todo.views import TodoListCreateView

urlpatterns = [
    path('add', TodoListCreateView.as_view()),
]

