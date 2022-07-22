from django.http import HttpResponse
from django.shortcuts import render
from .models import Question

# Create your views here.
def index(request):
    result = [x for x in Question.objects.all()]
    return HttpResponse(result)

def details(request, question_id):
    return HttpResponse("You are looking at the questions {}".format(question_id))

def results(request, question_id):
    return HttpResponse("The results of the question are {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("The choices of the questions are {}".format(question_id))