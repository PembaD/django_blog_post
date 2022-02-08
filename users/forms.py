from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#class inheritance used to create the registration form 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text="We recommend using gmail")

    class Meta: 
        model = User # .save() is make instance of the mode 'User'
        fields = ['username','email','password1','password2']

#create a new form to update the profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#new form for the profile model
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']