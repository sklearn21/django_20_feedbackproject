from django import forms
from django.core import validators  # For inbuilt implicit validation core module


# def starts_with_d(value):
#     if value[0].lower() != 'd':
#         raise forms.ValidationError('Name should with d')
#
#
# def name_without_number(value):
#     if value.isalpha() != True:
#         raise forms.ValidationError('Name should not contain numbers.')
#
#
def gmail_verification(value):
    if value[len(value) - 9:] != 'gmail.com':
        raise forms.ValidationError('Email must be gmail.')


class FeedBackForm(forms.Form):
    name = forms.CharField() #validators=[starts_with_d, name_without_number]

    rollno = forms.IntegerField()
    email = forms.EmailField(validators=[gmail_verification])

    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)

    feedback = forms.CharField(widget=forms.Textarea,
                               validators=[validators.MaxLengthValidator(40),
                                           validators.MinLengthValidator(10), ])
    bot_handler = forms.CharField(required=False, widget= forms.HiddenInput)

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

#................................................................................

    def clean(self):
        print('Total form validation.')
        cleaned_data = super().clean()
        bot_handler_value = cleaned_data['bot_handler']
        if len(bot_handler_value) > 0:
            raise forms.ValidationError('Thanks Bot!!')
        inputname = cleaned_data['name']
        if len(inputname) < 10 :
            raise forms.ValidationError('Name should compulsory contain min. 10 chars')
        inputrollno = cleaned_data['rollno']
        if len(str(inputrollno)) != 3:
            raise forms.ValidationError('Roll no should contain exact 3 digit.')

        inputpassword = cleaned_data['password']
        inputrpassword= cleaned_data['rpassword']

        if inputpassword != inputrpassword:
            raise forms.ValidationError('Password does not match')