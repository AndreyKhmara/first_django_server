from rest_framework import generics
from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        print("🔥 POPAL V CREATE!")  # 1 — Проверяем вход
        print("📦 DATA:", request.data)  # 2 — payload

        return super().create(request, *args, **kwargs)