from django import forms

from .models import Submission

class SubmissionForm(forms.ModelForm):
    CHOICE = [
        ('python3','python3'),
        ('cpp','cpp'),
        ('c','c'),
        ('java','java'),
        ('csharp','csharp'),
        ('go','go'),
        ('ruby','ruby'),
        ('php','php'),
        ('rust','rust'),
        ('javascript','javascript'),
        ('bash','bash'),
    ]
    language = forms.ChoiceField(
        label='language',
        required=True,
        disabled=False,
        initial=['python3'],
        choices=CHOICE,
        widget=forms.Select(attrs={'id': 'one',}))
    class Meta:
        model = Submission
        fields = ('language','code')