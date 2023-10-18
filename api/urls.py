from django.urls import path
from api.views import users_list

urlpatterns = [
    path('users_list', users_list, name="Users List"),
]
