from django.shortcuts import render
from rest_framework import viewsets
from .models import Contactus
from .serializers import ContactUsSerializer
# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = Contactus.objects.all()
    serializer_class = ContactUsSerializer