from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import data
from django.shortcuts import render
from gtts import gTTS
import io
from .forms import TextToSpeechForm

# Create your views here.
def index(request):
    dict_dept={
        'dept':data.objects.all()
    }
    return render(request,"index.html",dict_dept)

# views.py
from django.shortcuts import render
from .forms import TextToSpeechForm
def text_to_speech(request):
    if request.method == 'POST':
        form = TextToSpeechForm(request.POST)
        if form.is_valid():
            words = form.cleaned_data['words']
            # Perform further processing as needed
            return render(request, 'index.html', {'words': words})
    else:
        form = TextToSpeechForm()
    return render(request, 'input_form.html', {'form': form})
from .models import Word
from .forms import WordForm

def word_list(request):
    words = Word.objects.all()
    return render(request, 'word_list.html', {'words': words})

def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = WordForm()
    return render(request, 'add_word.html', {'form': form})