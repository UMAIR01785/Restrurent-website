from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from . forms import VendorForm
from . models import Vendor
from accounts.models import Userprofile
from accounts.forms import UserprofileForm

# Create your views here.
def profile(request):
    profile=get_object_or_404(Userprofile,user=request.user)
    vendor=get_object_or_404(Vendor,user=request.user)
    if request.method == "POST":
        user_form=UserprofileForm(request.POST,request.FILES,instance=profile)
        vnedor_form=VendorForm(request.POST,request.FILES,instance=vendor)
        if user_form.is_valid() and vnedor_form.is_valid():
            user_form.save()
            vnedor_form.save()
            messages.success(request, 'sucess update the profile!')
            return redirect('profile')
        else:
            print(user_form.errors)

    else:
        user_form=UserprofileForm(instance=profile)
        vnedor_form=VendorForm(instance=vendor)


    
    context={
        'profile':profile,
        'vendor': vendor,
        'user_form': user_form,
        'vnedor_form':vnedor_form,
    }

    return render(request,'vendor/profile.html',context)