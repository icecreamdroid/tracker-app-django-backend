from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from users.models import User

class Habit(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=30, default='',
                            verbose_name='Habit name')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['created']


class Log(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE,related_name='habit')
    

    def __str__(self) -> str:
        return self.habit.name


# Create your models here.
