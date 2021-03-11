from django import forms


class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, max_length=200, )

    # Explicit Validation Example................................................................

    def clean_name(self):
        inputname = self.cleaned_data['name']
        print('Validating name.')
        if len(inputname) < 4:
            raise forms.ValidationError('The length of name field should be greater than 4.')
        return inputname

    def clean_rollno(self):
        inputrollno = self.cleaned_data['rollno']
        print('Validating roll no.')
        return inputrollno

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        print('Validating email')
        return inputemail

    def clean_feedback(self):
        inputfeedback = self.cleaned_data['feedback']
        print('Validating feedback')
        return inputfeedback
