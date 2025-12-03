from django.urls import path
from todo.views import TodoListCreateView, ToggleTodoCompleteView, TodoDetailView

urlpatterns = [
    path("", TodoListCreateView.as_view()),  # GET/POST → /todo/
    path("completed/<int:id>", ToggleTodoCompleteView.as_view()),  # PATCH /todo/completed/<id>/
    path("<int:id>", TodoDetailView.as_view()),  # DELETE /todo/<id>/
]
