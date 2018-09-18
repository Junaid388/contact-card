from django import forms
from .models import Post

class MyModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['First_Name','Last_Name','Email_Address','Phone_Number','Category']
