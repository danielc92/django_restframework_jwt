from django.shortcuts import render
from rest_framework import viewsets
from .modesl import Language
from .serializer import LanguageSerializer

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
