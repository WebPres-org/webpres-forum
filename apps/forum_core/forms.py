from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', )

###
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.forum_core.models import Profile
from apps.forum_core import models



###edit profile form
class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'A user with that username already exists.')
        return username

##################

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

##Add New
class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Profile
        fields = ['bio', 'avatar', 'facebook_url', 'twitter_url','website_url', 'instagram_url' ]


class ProfilePageForm(forms.ModelForm):
    model = Profile
    fields = ['bio', 'avatar', 'facebook_url', 'twitter_url','website_url', 'instagram_url' ]
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
