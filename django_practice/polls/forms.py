from django import forms
from .models import Suggestion

class suggestion(forms.ModelForm):
    template_name = 'polls/suggestion.html'
    name = forms.CharField(label='Name:')
    suggestion_body = forms.CharField(widget=forms.Textarea, label='Suggestion:')

    class Meta:
        model = Suggestion
        fields = ('name', 'suggestion_body',)
