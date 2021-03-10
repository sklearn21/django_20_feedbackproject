from django.shortcuts import render
from . import forms

# Create your views here.


def feedback_view(request):
    form = forms.FeedBackForm()
    return render(request, 'testapp/feedback.html', {'form': form})
