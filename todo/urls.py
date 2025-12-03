from django.urls import path
from todo.views import TodoListCreateView, ToggleTodoCompleteView, TodoDetailView, EditTodoCompleteView

urlpatterns = [
    path("", TodoListCreateView.as_view()),  # GET/POST → /todo/
    path("completed/<int:id>", ToggleTodoCompleteView.as_view()),  # PATCH /todo/completed/<id>/
    path("edit/<int:id>", EditTodoCompleteView.as_view()),
    path("<int:id>", TodoDetailView.as_view()),  # DELETE /todo/<id>/
]
