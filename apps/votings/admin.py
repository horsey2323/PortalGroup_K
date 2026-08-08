from django.contrib import admin

from .models import Answer, Choice, Question, Survey, SurveyCompletion


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'allow_retake', 'created_at')
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'survey', 'question_type', 'order')
    inlines = [ChoiceInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'session_key', 'created_at')
    list_filter = ('question__survey',)


@admin.register(SurveyCompletion)
class SurveyCompletionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'user', 'session_key', 'completed_at')
    list_filter = ('survey',)

