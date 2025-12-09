from django.shortcuts import render,redirect
from . forms import Userform
from . models import User,Userprofile
from django.contrib import messages,auth
from vendor.forms import VendorForm
from . utils import detectuser,send_verfication_email,reset_password_email
from django.contrib.auth.decorators import login_required , user_passes_test
from django.core.exceptions import PermissionDenied
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from vendor.models import Vendor

def check_role_vendor(user):
      if user.role == 2:
            return True
      else:
            raise PermissionDenied
      
def check_role_customer(user):
      if user.role == 1:
            return True
      else:
            raise PermissionDenied

# Create your views here.
def registeruser(request):
    if request.user.is_authenticated:
            messages.warning(request,"YOu already in login")
            return redirect('Myaccounts')
    elif request.method == "POST":
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
              user.role=User.Customer
              
              user.save()
              send_verfication_email(request,user)
              messages.success(request,"Register is successful")
              return redirect('login')
         else:
              print(form.errors)
                
    else:
          form=Userform()

    context={
        'form': form
    }
    return render(request,'accounts/registeruser.html',context)


def registervendor(request):
     if request.user.is_authenticated:
            messages.warning(request,"YOu already in login")
            return redirect('Myaccounts')

     elif request.method == "POST":
          form=Userform(request.POST)
          v_form=VendorForm(request.POST,request.FILES)

          if form.is_valid() and v_form.is_valid():
               password=form.cleaned_data.get('password')
               user=form.save(commit=False)
               user.set_password(password)
               user.role=User.Restaurant
               
               user.save()
               vendor=v_form.save(commit=False)
               vendor.user=user
               user_profile=Userprofile.objects.get(user=user)
               vendor.user_profile=user_profile
               vendor.save()

               send_verfication_email(request,user)
               messages.success(request,"Registion is successfull please wait for the approal!")
               return redirect ('registervendor')
          
          
     
          else:
                print(form.errors)
     
     
     
     
     else:
               form=Userform()
               v_form=VendorForm()


     context={
          'form':form,
          'v_form':v_form,
     }
     
     return render(request,'accounts/registervendor.html',context)


def login(request):
      if request.user.is_authenticated:
            messages.warning(request,"YOu already in login")
            return redirect('Myaccounts')
      elif request.method == "POST":
            email=request.POST.get('email')
            password=request.POST.get('password')
            user=auth.authenticate(request,email=email,password=password)
            if user is not None:
                  auth.login(request,user)
                  messages.success(request,'Login sucessful')
                  return redirect('Myaccounts')
            else:
                  messages.error(request,'Invaild login!')
                  return redirect('login')
      return render(request,'accounts/login.html')


@login_required(login_url='login')
def logout(request):
      auth.logout(request)
      messages.success(request,'sucessful logout!')
      return redirect('login')


@login_required(login_url='login')
@user_passes_test(check_role_customer)
def cusdashboard(request):
      return render(request,'accounts/cusdashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendordashboard(request):
      vendor=Vendor.objects.get(user=request.user)
      context={
            'vendor':vendor
      }

      return render(request,'accounts/vendordashboard.html',context)

@login_required(login_url='login')
def Myaccounts(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    redirect_url = detectuser(user)
    return redirect(redirect_url) 



def activate(request,uid64,token):
      try:
            uid= urlsafe_base64_decode(uid64).decode()
            user=User._default_manager.get(pk=uid)
      except(TypeError,ValueError,OverflowError,User.DoesNotExist):
            user=None
           
      if user is not None and default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            messages.success(request,'sucessfull active the account')
            return redirect('login')
      else:
             messages.error(request,'Invalid details')
             return redirect('registerUser')
      

def forgot(request):
      if request.method == "POST":
            email = request.POST.get('email')
            if User.objects.filter(email=email).exists():
                  user = User.objects.get(email__exact=email)

                  reset_password_email(request,user)
                  messages.success(request, 'Password reset link is sent to your Email!')
      return render(request,'accounts/forgot.html')

def reset(request):
      return render(request,'accounts/forgot.html')


def reset_password(request,uid64,token):
      try:
            uid=urlsafe_base64_decode(uid64).decode()
            user= User._default_manager.get(pk=uid)
      except(ValueError,TypeError,User.DoesNotExist):
            user=None

      if User is not None and default_token_generator.check_token(user,token):
            request.session['uid'] = uid
            messages.info(request,'Please reset the password!')
            return redirect('reset')
      return render(request,'accounts/forgot.html')

def reset(request):
      if request.method == "POST":
            password = request.POST.get('password')
            confirme_password=request.POST.get('confim_password')
            if password == confirme_password:
                  pk = request.session['uid']
                  user= User.objects.get(pk=pk)
                  user.set_password(password)
                  user.save()
                  messages.success(request,'Sucessfull update the password')
                  return redirect('login')
            else:
               messages.error(request,'Password does not match !')
               return redirect('reset')
      return render(request ,'accounts/password_reset.html')

