from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from habit_tracker.serializers import GroupSerializer, HabitSerializer, LogSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from habit_tracker.models import Habit, Log
import datetime

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from users.models import User
from django.utils import timezone
import json

User = get_user_model()


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class habit_list(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    # permission_classes=[permissions.IsAuthenticated]

    def get(self, request, user):
        print(request.user)
        habits = Habit.objects.filter(User=user)
        serializer = HabitSerializer(habits, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.user.is_authenticated)
        data = JSONParser().parse(request)
        serializer = HabitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


class habit_detail(APIView):
    """
    Retrieve, update or delete a code snippet.
    """

    def dispatch(self, request, pk):

        try:
            global snippet
            snippet = Habit.objects.get(pk=pk)
        except Habit.DoesNotExist:
            return HttpResponse(status=404)

    def get():
        serializer = HabitSerializer(snippet)

        return JsonResponse(serializer.data)

    def post(self, request, pk):
        data = JSONParser().parse(request)
        print(data)
        # serializer = HabitSerializer(snippet, data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data)
        return JsonResponse(status=400)

    def delete():
        Habit.delete()
        return HttpResponse(status=204)


class logs(APIView):

    def get(self, request, habit):
        try:
            global logs
            logs = Log.objects.filter(habit=habit)
        except:
            return HttpResponse(status=404)
        print(logs)
        serializer = LogSerializer(logs,many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, habit):
        habitInstance = Habit.objects.get(pk=habit)
        validated_data = {'habit': habitInstance.pk}
        serializer = LogSerializer(data=validated_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors)
