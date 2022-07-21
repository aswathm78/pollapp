from secrets import choice
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published", auto_now=False, auto_now_add=False)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice = models.CharField( max_length=200)
    votes = models.IntegerField(default=0)