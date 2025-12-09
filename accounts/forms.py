from django import forms
from . models import User,Userprofile
from accounts.validators import validator_error
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
    
    def __init__(self,*args,**kwargs):
         super().__init__(*args,**kwargs)
         
         self.fields['first_name'].widget.attrs['placeholder']='Enter the First name'
         self.fields['last_name'].widget.attrs['placeholder']='Enter the last name'
         self.fields['email'].widget.attrs['placeholder']='Enter the Email'
         self.fields['username'].widget.attrs['placeholder']='Enter the Username'


         for item in self.fields:
              self.fields[item].widget.attrs['class']='form-control'

class UserprofileForm(forms.ModelForm):
     profile_pic = forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}),validators=[validator_error])
     cover_pic = forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}),validators=[validator_error])
     address=forms.CharField(widget=forms.TextInput(attrs={
          'placeholder':'Start typing ...','required':'required'
     }), max_length=250, required=False)
     class Meta:
          model= Userprofile
          fields=['profile_pic','cover_pic','address','country','state','pin_code','latitude','longitude']