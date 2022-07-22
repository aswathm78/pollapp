from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("hi")

def details(request, question_id):
    return HttpResponse("You are looking at the questions {question_id}")

def results(request, question_id):
    return HttpResponse("The results of the question are {question_id}")

def vote(request, question_id):
    return HttpResponse("The choices of the questions are {question_id}")