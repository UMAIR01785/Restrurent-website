from django import forms
from . models import Vendor


class VendorForm(forms.ModelForm):

    class Meta:
        model=Vendor

        fields=['vendor_name','vendor_licience']



    def __init__(self,*args,**kwargs):
            super(VendorForm,self).__init__(*args,**kwargs)


            self.fields['vendor_name'].widget.attrs['placeholder']='Enter the vendor name'


