from django.utils import timezone
from secrets import choice
from django.db import models
from datetime import timedelta

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published", auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.DO_NOTHING)
    choice = models.CharField( max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice
    