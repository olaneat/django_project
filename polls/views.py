from django.shortcuts import get_object_or_404, render
from .models import Choice, Question
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:4]
	context = {	'latest_question_list': latest_question_list,}
	return render(request, 'polls/index.html', context,)
	return HttpResponse("I'm good to Go")

def detail(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	question = Question.objects.get(pk=question_id)		
	#return HttpResponse ("You're voting on question %s." % question_id)
	return render (request, 'polls/detail.html', {'question': question})

def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})
	
def vote(request, question_id):
	question = get_object_or_404(Question, pk= question_id)
	try: 
		selected_choice = question.choice_set.get (pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
		'question':question,
		'error_message': "You didn't select a choice",
		})	
	else:
		selected_choice.vote +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))	






# Create your views here.
