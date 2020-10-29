from django import forms
from .models import RegistrationData


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Please enter your username'
                               }))

    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Please enter your password'
                               }))
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Please enter your e-mail (We do NOT share your e-mail with anyone)'
                            }))

    phone = forms.CharField(max_length=100,
                            widget=forms.NumberInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Type in your phone number',

                            }))


class RegistrationModal(forms.ModelForm):

    class Meta:

        model = RegistrationData

        fields = [
            'username',
            'password',
            'email',
            'phone'

        ]

        widgets = {
            'username': forms.TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'username'

            }),

            'password': forms.PasswordInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'password'
            }),

            'email': forms.EmailInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'email'
            }),

            'phone': forms.NumberInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'phone'
            })
        }
