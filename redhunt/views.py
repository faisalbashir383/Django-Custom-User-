from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrganisationSerializer,UserSerializer
from .models import Organisation,User
import datetime
# Create your views here.


class OrganisationView(viewsets.ModelViewSet):
     queryset = Organisation.objects.all()

     serializer_class = OrganisationSerializer


class UserView(viewsets.ModelViewSet):
     queryset = User.objects.all()   
     serializer_class = UserSerializer     