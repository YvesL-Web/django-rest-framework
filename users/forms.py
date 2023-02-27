# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from .models import User

# class UserRegisterForm(UserCreationForm):
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control shadow',"placeholder":"Password"}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control shadow',"placeholder":"Confirm Password"}))
#     class Meta:
#         model = User
#         fields = ['username','first_name','last_name','email','password1','password2']

#         widgets= {
#             'username' : forms.TextInput(attrs={'class':'form-control shadow','placeholder':'Username'}),
#             'first_name' :forms.TextInput(attrs={'class':'form-control shadow','placeholder':'First name'}),
#             'last_name' :forms.TextInput(attrs={'class':'form-control shadow','placeholder':'Last name'}),
#             'email' :forms.EmailInput(attrs={'class':'form-control shadow','placeholder':'Email'}),
#         }