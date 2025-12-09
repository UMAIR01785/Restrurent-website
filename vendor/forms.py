from django import forms
from . models import Vendor
from accounts.validators import validator_error

class VendorForm(forms.ModelForm):

    class Meta:
        model=Vendor

        fields=['vendor_name','vendor_licience']



    def __init__(self,*args,**kwargs):
            
            super(VendorForm,self).__init__(*args,**kwargs)
            self.fields['vendor_licience']  = forms.FileField(widget=forms.FileInput(attrs={'class':'btn-btn-info'}),validators=[validator_error])


            self.fields['vendor_name'].widget.attrs['placeholder']='Enter the vendor name'


