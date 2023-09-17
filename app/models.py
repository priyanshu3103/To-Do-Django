from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    status_choice = [
    ("C", "COMPLETE"),
    ("P", "PENDING")
    ]
    priority_choice = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10","10")
    ]
    titel = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority= models.CharField(max_length=2, choices=priority_choice)

