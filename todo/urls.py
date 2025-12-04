from django.urls import path
from todo.views import TodoListCreateView, TodoDetailView

urlpatterns = [
    path("", TodoListCreateView.as_view()),        # GET, POST
    path("<int:id>", TodoDetailView.as_view()),    # GET, PATCH, DELETE
]