from django.urls import path
from habit_tracker import views

urlpatterns = [
    path('habits/', views.habit_list.as_view())
]