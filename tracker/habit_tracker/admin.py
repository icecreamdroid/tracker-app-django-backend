from django.contrib import admin
from users.models import User
from habit_tracker.models import Habit,Log


admin.site.register(User)
admin.site.register(Log)
admin.site.register(Habit)

# Register your models here.
