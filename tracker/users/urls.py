from django.urls import path
from habit_tracker import views
from . import views as userViews

urlpatterns = [
    path('habits/', views.habit_list.as_view()),
    path('signup/', userViews.RegisterView.as_view()),
    path('login/', userViews.LoginView.as_view()),
    path('signup/',userViews.RegisterView.as_view())
]
