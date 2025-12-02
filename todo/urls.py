from django.urls import path
from todo.views import TodoListCreateView

urlpatterns = [
    path("", TodoListCreateView.as_view()),       # GET/POST → /todo/
]

