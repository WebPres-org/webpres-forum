from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django import  forms
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    
    image = models.ImageField(upload_to="images",default="default/user.png")
    
    
class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")
    
class Replie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp= models.DateTimeField(default=now)
    image = models.ImageField(upload_to="images",default="")


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads",default="default/user.png")


    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image

## User Update Profile
class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    twitter_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'website_url', 'facebook_url', 'twitter_url',  'instagram_url' ]


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    website_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))
    facebook_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))

    instagram_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 1}))

    class Meta:
        model = User
        fields = ['username', 'email', 'instagram_url','facebook_url']

