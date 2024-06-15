from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import Todo, Person


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = ['identifier', 'deadline', 'description', 'shared_from']
        extra_kwargs = {'shared_from': {'required': False}}


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['username', 'email', 'birthdate', 'profileId', 'first_name', 'last_name']
