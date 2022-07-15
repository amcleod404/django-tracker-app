from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models


# class Workout(models.Model):
#   name = models.CharField(max_length=50)
#   description = models.CharField(max_length=150)
#   completed = models.BooleanField(default=False)
#   created_at = models.DateTimeField(auto_now_add=True)
#   created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Exercise(models.Model):
  name = models.CharField(max_length=100)
  sets = models.PositiveIntegerField()
  reps = models.PositiveIntegerField()
  weight = models.PositiveIntegerField()
  performed = models.DateTimeField(auto_now_add=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  # workout = models.ForeignKey(Workout, on_delete=models.CASCADE,null= True, default=None)

  def __str__(self):
        return self.name