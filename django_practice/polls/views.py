from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question, Suggestion
from .forms import suggestion


def suggest_view(request):
    if request.method == 'GET':
        form = suggestion()
        return render(request, 'polls/suggestion.html', {'form':form})

    if request.method == 'POST':
        form = suggestion(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            text = form.cleaned_data['suggestion_body']

            form = suggestion()
            args = {'form': form, 'name': name, 'text': text}
            return render(request, 'polls/suggestion.html', args)
        return render(request, 'polls/suggestion.html', {'form': form})


def suggest_list_view(request):
    if request.method == 'GET':
        s = Suggestion.objects.all()
        context = {
            's': s
        }
        return render(request, 'polls/list.html', context)

# class AllSuggestionsView(generic.ListView):
#     template_name = 'polls/list.html'
#     context_object_name = 'suggestions_list'
#
#     def get_queryset(self):
#         return Suggestion.objects.all()


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))