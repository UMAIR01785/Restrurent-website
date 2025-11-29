from django import forms
from . models import User

class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control small-input',
        'placeholder':'Entre the password',
    }),max_length=50,required=True)
    confirmed_password=forms.CharField(widget=forms.PasswordInput(attrs={
         'class':'form-control small-input',
        'placeholder':'Entre the password',
    }),max_length=50,required=True)
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','phone_number','password']

    def clean(self):
            cleaned_data=super().clean()
            password=cleaned_data.get('password')
            confirmed_password=cleaned_data.get('confirmed_password')

            if password != confirmed_password:
                raise forms.ValidationError("password does not match")
            
            return cleaned_data