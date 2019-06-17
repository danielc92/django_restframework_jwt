from rest_framework import serializers
from .models import Language, Programmer

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'year', 'developer_company', 'predescessors')


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'first_name', 'last_name', 'languages', 'created_at', 'modified_at')