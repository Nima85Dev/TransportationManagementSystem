from django import forms
from accounts.models import ProfileModel
from django.contrib.auth.forms import UserChangeForm
from captcha.fields import CaptchaField

class ProfileRegisterForm(forms.ModelForm):
  class Meta:
    model = ProfileModel
    fields=['ProfileImage','Credit','Gender']
    
  first_name = forms.CharField(max_length=100)
  last_name= forms.CharField(max_length=100)
  username = forms.CharField(max_length=100)
  password = forms.CharField(widget=forms.PasswordInput)
  email = forms.CharField(widget=forms.EmailInput)
  captcha = CaptchaField()
  
  
    
class ProfileEditForm(forms.ModelForm):
  class Meta:
    model = ProfileModel
    fields = ['ProfileImage','Credit','Gender']
    
class UserEditForm(UserChangeForm):
  class Meta(UserChangeForm.Meta):
    fields = ["first_name","last_name","email"]
  password = None