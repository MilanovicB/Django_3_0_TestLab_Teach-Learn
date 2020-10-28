from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Please enter your username'
                               }))

    password = forms.CharField(max_length=64,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Please enter your password'
                                }))
    email = forms.CharField(max_length=64,
                            widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Please enter your e-mail (We do NOT share your e-mail with anyone)'
                            }))

    phone = forms.CharField(max_length=64,
                            widget=forms.NumberInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Type in your phone number',

                            }))
