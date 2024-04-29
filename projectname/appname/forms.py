# forms.py
from django import forms

class TextToSpeechForm(forms.Form):
    words = forms.CharField(
        label='abc:apple beetrot carrot',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50})
    )

class TextToSpeechForm(forms.Form):
    words = forms.CharField(
        label='check',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 50})
    )
    
from django import forms
from .models import Word

class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = ['word']
