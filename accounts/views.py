from django.shortcuts import render,redirect
from . forms import Userform
from . models import User
from django.contrib import messages
# Create your views here.
def registeruser(request):
    if request.method == "POST":
         form = Userform(request.POST)
         if form.is_valid():
              first_name=form.cleaned_data['first_name']
              last_name=form.cleaned_data['last_name']
              email=form.cleaned_data['email']
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              user=User.objects.create_user(
                   first_name=first_name,
                   last_name=last_name,
                   password=password,
                   email=email,
                   username=username,
              )
              user.role='customer'
              user.save()
              messages.success(request,"Register is successful")
              return redirect('registeruser')
         else:
              print(form.errors)
                
    else:
          form=Userform()

    context={
        'form': form
    }
    return render(request,'accounts/registeruser.html',context)