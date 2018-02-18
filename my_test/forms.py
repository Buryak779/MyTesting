from django.forms import ModelForm
from . models import Vote


class AnswerForm(ModelForm):
    """Форма ввода ответа
     для сравнения"""
    class Meta:
        model = Vote
        fields = ('answer_true',)
