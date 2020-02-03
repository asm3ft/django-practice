from django.contrib import admin

from .models import Choice, Question, Suggestion


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra= 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class SuggestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['suggestion_text']}),
        (None,                  {'fields': ['name_text']}),
    ]
    list_display = ('name_text', 'suggestion_text')
    search_fields = ['name_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Suggestion, SuggestionAdmin)