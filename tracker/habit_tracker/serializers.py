from django.contrib.auth.models import User, Group
from rest_framework import serializers
from habit_tracker.models import Habit, Log
from json import dumps
from django.utils import timezone


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class HabitSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Habit
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    
    def create(self,validated_data):
        habit = validated_data['habit']
        logObject=Log.objects.create(habit=habit)
        return logObject

    class Meta:
        model = Log
        fields = ('habit','created')
