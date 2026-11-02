from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['password'].widget.attrs['placeholder'] = '••••••••'


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'bio', 'avatar')


    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
                
            self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
            self.fields['email'].widget.attrs['placeholder'] = 'name@example.com'
            self.fields['first_name'].widget.attrs['placeholder'] = 'Enter your first name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Enter your last name'
            self.fields['password1'].widget.attrs['placeholder'] = '••••••••'
            self.fields['password2'].widget.attrs['placeholder'] = '••••••••'