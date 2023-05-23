from django.urls import path
from habit_tracker import views

urlpatterns = [
    path('users/<int:user>/habits/', views.habit_list.as_view()),
    path('habits/<int:pk>/', views.habit_detail.as_view()),
    path('habits/<int:habit>/logs/',views.logs.as_view())
    # path('habitset/',views.UserViewSet.as_view({'get':'list'}))
]