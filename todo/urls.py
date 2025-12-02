from django.urls import path
from todo.views import TodoListCreateView, ToggleTodoCompleteView

urlpatterns = [
    path("", TodoListCreateView.as_view()),  # GET/POST → /todo/
    path("completed/<int:id>", ToggleTodoCompleteView.as_view()),  # PATCH /todo/completed/<id>/
]
