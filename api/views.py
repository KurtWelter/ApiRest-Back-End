from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import User
from .serializers import UserSerializer



# Create your views here.
@csrf_exempt
@api_view(['GET'])
def users_list(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        # Obtiene los datos del usuario del cuerpo de la solicitud
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            # Guarda el nuevo usuario en la base de datos
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
