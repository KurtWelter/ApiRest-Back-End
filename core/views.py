from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
  users = User.objects.all()

  datos = {
    'users' : users
  }
  return render(request,)