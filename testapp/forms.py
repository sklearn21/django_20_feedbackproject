from django import forms

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    feedback=forms.CharField(widget=forms.Textarea, max_length= 200,)