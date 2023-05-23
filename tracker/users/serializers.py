from rest_framework import serializers
# from .models import User
from habit_tracker.models import Habit
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    habits = serializers.StringRelatedField(
        allow_null=True, many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'name', 'habits',)
