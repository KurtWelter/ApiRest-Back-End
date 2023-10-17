from rest_framework import serializers
from .models import Register
from .models import Login

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Register
    fields = ['id','teacher','student','name','lastname','email','password']

class LoginSerializer(serializers.ModelSerializer):
  model = Login
  fields = ['id','email','password']    