from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
    )
    username = forms.CharField(
        label='Enter username',
        required=True,
        help_text='Cannot contain characters: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Enter password',
        required=True,
        help_text='Password must not be short and simple',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'})
    )
    username = forms.CharField(
        label='Enter username',
        required=True,
        help_text='Cannot contain characters: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Upload photo',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']