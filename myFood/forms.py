from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'requried': '',
            'name': 'username',
            'id':'form3Example1c',
            'type': 'text',
            'class': 'form-control',
            'placeholder':'Enter your name'
        })
        self.fields["email"].widget.attrs.update({
            'requried': '',
            'name': 'email',
            'id':'form3Example3c',
            'type': 'email',
            'class': 'form-control',
            'placeholder':'Enter your E-Mail'
        })
        self.fields["password1"].widget.attrs.update({
            'requried': '',
            'name': 'password1',
            'id':'form3Example4c',
            'type':'password',
            'class': 'form-control',
            'placeholder':'Enter your Password'
        })
        self.fields["password2"].widget.attrs.update({
            'requried': '',
            'name': 'password2',
            'id':'form3Example4cd',
            'type': 'password',
            'class': 'form-control',
            'placeholder':'Confirm your password'
        })

    
    class Meta:
        model = User
        fields = ('username','email','password','password2')