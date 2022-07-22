from django.template import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Question

from django.shortcuts import render


# Create your views here.
def index(request):
    result = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'result': result,
    }
    return render(request,'polls/index.html',context)

def details(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("That id does not exist")
    return render(request, 'polls/details.html', context={'question': question})


def results(request, question_id):
    return HttpResponse("The results of the question are {}".format(question_id))

def vote(request, question_id):
    return HttpResponse("The choices of the questions are {}".format(question_id))