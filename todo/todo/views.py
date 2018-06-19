from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDoElements


class ToDoView(APIView):
    def get(self, request):
        todos = ToDoElements.objects.all()
        serilizers = ToDoSerializer(todos, many=True)
        return Response(serilizers.data)
