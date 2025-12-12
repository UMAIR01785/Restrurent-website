from django.shortcuts import render
from vendor.models import Vendor
def home(request):
    vendor=Vendor.objects.filter(is_active=True,user__is_active=True)
    context={
        'vendor':vendor
    }
    return render(request,'home.html',context)
