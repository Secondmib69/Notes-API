from rest_framework import serializers
from .models import Note
# from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField
from taggit.serializers import TaggitSerializer, TagListSerializerField
from django.contrib.auth import get_user_model, password_validation



User = get_user_model()

class NoteSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created', 'updated', 'tags', 'user']
        read_only_fields = ['user']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True, validators=[password_validation.validate_password])
    password2 = serializers.CharField(required=True, write_only=True, label='Confirm Password')
    notes = serializers.HyperlinkedIdentityField(view_name='note:user-note-list', lookup_url_kwarg = 'id')
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password2', 'is_staff', 'notes']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Passwords don\'t match')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        return user
