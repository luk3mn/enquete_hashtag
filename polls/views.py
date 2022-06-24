from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question

# Create your views here.

# Criar uma visualização para a página inicial
def index(request): # 'request' quando estiver fazendo uma tentativa de acessar o site
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     return HttpResponse('Essa é a pergunta de número {}'.format(question_id))

def results(request, question_id):
    question = Question(id=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request,'polls/vote.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))