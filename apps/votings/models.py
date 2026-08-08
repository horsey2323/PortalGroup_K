from django.db import models
from django.conf import settings

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    allow_retake = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Question(models.Model):
    TEXT = 'text'
    SINGLE_CHOICE = 'single'
    MULTI_CHOICE = 'multi'

    QUESTION_TYPES = [
        (TEXT, 'Текстовый ответ'),
        (SINGLE_CHOICE, 'Один вариант'),
        (MULTI_CHOICE, 'Несколько вариантов'),
    ]

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default=SINGLE_CHOICE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    session_key = models.CharField(max_length=40, null=True, blank=True)

    text_answer = models.TextField(blank=True, null=True)
    selected_choices = models.ManyToManyField(Choice, blank=True, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer to "{self.question}" ({self.user or self.session_key})'


class SurveyCompletion(models.Model):

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='completions')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    session_key = models.CharField(max_length=40, null=True, blank=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['survey', 'user'],
                condition=models.Q(user__isnull=False),
                name='unique_survey_completion_per_user',
            ),
            models.UniqueConstraint(
                fields=['survey', 'session_key'],
                condition=models.Q(session_key__isnull=False),
                name='unique_survey_completion_per_session',
            ),
        ]

    def __str__(self):
        return f'{self.survey} completed by {self.user or self.session_key}'
