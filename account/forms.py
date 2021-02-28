from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

# fom pra criar o usuario personalizado
class UserCreationFormCustom(UserCreationForm):
    # personalizado o formulario
    email = forms.EmailField(max_length=100,  widget=forms.TextInput(attrs={'placeholder': 'Email...',}))
    username = forms.CharField(min_length=6 ,max_length=24, widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    
    class Meta:
        model = User
        # Fields do form
        fields = ['username', 'email', 'password1', 'password2']
    
    # Verifica de esse email ja esta sendo usado 
    def clean_email(self):
        ValidatioEmail = self.cleaned_data['email']
        # Verifica se o Email est em uso
        if User.objects.filter(email=ValidatioEmail).exists():
            raise ValidationError(f"O email {ValidatioEmail} ja esta em uso")
        # retorna ok
        return ValidatioEmail 

    # Verifica de esse Usernaem ja esta sendo usado     
    def clean_usernaem(self):
        ValidatioUsername = self.cleaned_data['username']
        # Verifica se o Email esta em uso
        if User.objects.filter(username==ValidatioUsername).exists():
            raise ValidationError(f"O Username {ValidatioUsername} ja esta em uso")
        # retorna ok
        return ValidatioUsername 
