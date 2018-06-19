from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDoElements


class ToDoView(APIView):
    def get(self, request):
        todos = ToDoElements.objects.all()
        serilizers = ToDoSerializer(todos, many=True)
        return Response(serilizers.data)

    def put(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)