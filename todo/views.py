from rest_framework import generics
from todo.models import Todo
from todo.serializers import TodoSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all() # в теории вот это для GET (получение всех todo)
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs): #  def create для POST (Создание todo)
        print("🔥 POPAL V CREATE!")
        print("📦 DATA:", request.data)
        return super().create(request, *args, **kwargs)