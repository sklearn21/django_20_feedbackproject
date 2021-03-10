from django.shortcuts import render
from . import forms


# Create your views here.


def thank_you(request):
    return render(request,'testapp/thank_you.html')

def feedback_view(request):
    form = forms.FeedBackForm()
    if request.method == 'POST':
        form = forms.FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing Feedback info')
            print('Student Name: ', form.cleaned_data['name'])
            print('Student Roll No.: ', form.cleaned_data['rollno'])
            print('Student E-mail: ', form.cleaned_data['email'])
            print('Student Feedback: ', form.cleaned_data['feedback'])
            thank_you(request)

    return render(request, 'testapp/feedback.html', {'form': form})
