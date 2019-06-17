from rest_framework import serializers
from .models import Language, Programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'year', 'developer_company', 'predescessors')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'first_name', 'last_name', 'languages', 'craeted_at', 'modified_at')