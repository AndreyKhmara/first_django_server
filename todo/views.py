from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):  # def create для POST (Создание todo)
        return super().create(request, *args, **kwargs)


class ToggleTodoCompleteView(APIView):
    def patch(self, request, id, format=None):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

        # обновляем поле complete
        complete = request.data.get("complete")
        if complete is None:
            return Response({"error": "Missing 'complete' field"}, status=status.HTTP_400_BAD_REQUEST)

        todo.complete = complete
        todo.save()

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EditTodoCompleteView(APIView):
    def patch(self, request, id, format=None):
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

        # обновляем поле title
        title = request.data.get("title")
        if title is None:
            return Response({"error": "Missing 'complete' field"}, status=status.HTTP_400_BAD_REQUEST)

        todo.title = title
        todo.save()

        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)



class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'id'
