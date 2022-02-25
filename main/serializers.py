from dataclasses import fields
from rest_framework import serializers
from main.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')



