from django import forms
from model.contrib.auth.models import User
from app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username','email','password']


class UserProfileInfoForm(forms.ModelForm):
    #Nothing I wanna Modify

    class Meta():
        model = UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']
