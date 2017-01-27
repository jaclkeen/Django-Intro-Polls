from django.contrib import admin
from .models import Question

# Used to edit how the question admin form looks
# This is done by creating a new class and specifiying values
# If editing isn't neccessary just use 'admin.site.register(modelName)''

class QuestionAdmin(admin.ModelAdmin):
    # Changes order in which fields appear on admin page
    fields = ['pub_date', 'question_text']

    # Specifies the the fields that appear on the main modules page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    
    # That adds a filter sidebar that lets people filter the change list by the pub_date field:
    list_filter = ['pub_date']

    # Adds a search box at the top of the change list. When somebody enters search terms, Django will search the question_text field.
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
