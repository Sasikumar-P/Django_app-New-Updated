from django import forms
from django.contrib.auth.models import User
from sss.models import  UserProfile,Family

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
class FamilyForm(forms.ModelForm):
	class Meta:
		model = Family
		fields =('fathername','mothername','brothername','sistername','grandfathername','grandmothername','annualincome')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

