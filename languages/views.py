from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer
from .serializers import LanguageSerializer, ProgrammerSerializer

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ProgrammerView(viewsets.ModelViewSet):
    
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
