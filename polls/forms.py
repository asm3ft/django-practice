from django import forms
from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    template_name = 'polls/suggestion.html'
    # name = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class': 'form-control',
    #     }),
    #     label='Name:')
    # suggestion_body = forms.CharField(widget=forms.Textarea, label='Suggestion:')

    class Meta:
        model = Suggestion
        fields = ['name_text', 'suggestion_text']
