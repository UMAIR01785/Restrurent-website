from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from . forms import VendorForm
from . models import Vendor
from accounts.models import Userprofile
from accounts.forms import UserprofileForm
from menu.models import Category ,FoodItem
from django.contrib.auth.decorators import login_required , user_passes_test
from accounts.views import check_role_vendor
from menu.forms import CategoryForm,FooditmeForm
from django.template.defaultfilters import slugify
# Create your views here.
@login_required(login_url='login')
@user_passes_test(check_role_vendor)
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




@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def menu_builder(request):
    vendor=Vendor.objects.get(user=request.user)
    category=Category.objects.filter(vendor=vendor)
    context={
        'category': category,
        'vendor'  : vendor


    }
    return render(request,'vendor/menu_builder.html',context)

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def food_by_category(request, pk=None):
    vendor=Vendor.objects.get(user=request.user)
    category=Category.objects.get(vendor=vendor, pk=pk)
    fooditem=FoodItem.objects.filter(vendor=vendor,category=category)
    context={
        'fooditem':fooditem,
        'category': category,
        'vendor':vendor
    }
    return render(request,'vendor/menu_by_category.html',context)



def add_category(request):
    vendor=Vendor.objects.get()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category_name=form.cleaned_data['category_name']
            vendor=Vendor.objects.get(user=request.user)
            
            # Check if category already exists for this vendor
            if Category.objects.filter(vendor=vendor, category_name__iexact=category_name).exists():
                messages.error(request, 'Category with this name already exists!')
                return redirect('add_category')
            
            category=form.save(commit=False)
            category.vendor=vendor
            category.slug=slugify(category_name)
            category.save()
            messages.success(request,'Category created successfully!')
            return redirect('menu_builder')

    else:
        form=CategoryForm()


    context={
        'form':form,
        'vendor':vendor
        
    }
    return render(request,'vendor/add_category.html',context)


def edit_category(request,pk=None):
    vendor=Vendor.objects.get()
    category=get_object_or_404(Category,pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category_name=form.cleaned_data['category_name']
            vendor=Vendor.objects.get(user=request.user)
            category=form.save(commit=False)
            category.vendor=vendor
            category.slug=slugify(category_name)
            category.save()
            messages.success(request,'Category Updated  successfully!')
            return redirect('menu_builder')

    else:
        form=CategoryForm(instance=category)


    context={
        'form':form,
        'category':category,
        'vendor':vendor
        
    }

    return render(request,'vendor/edit_category.html',context)


def delete_category(request,pk=None):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    messages.success(request,'successfully delete !')
    return redirect('menu_builder')


def add_food(request):
    if request.method =="POST":
        form=FooditmeForm(request.POST , request.FILES)
        if form.is_valid():
            fooditem=form.cleaned_data['item_name']
            food = form.save(commit=False)
            food.vendor=Vendor.objects.get(user=request.user)
            food.slug=slugify(fooditem)
            food.save()
            messages.success(request,'Successfully add the food item!')
            return redirect ('food_by_category' ,food.category.id)
        else:
            print(form.errors)

            

    else:
        form=FooditmeForm()
    context={
        'form':form
    }
    return render(request,'vendor/add_food.html',context)


def edit_food(request,pk=None):
    vendor=Vendor.objects.get()
    food=get_object_or_404(FoodItem,pk=pk)
    if request.method == "POST":
        form = FooditmeForm(request.POST,request.FILES, instance=food)
        if form.is_valid():
            foodtitle=form.cleaned_data['item_name']
            vendor=Vendor.objects.get(user=request.user)
            fooD=form.save(commit=False)
            fooD.vendor=vendor
            fooD.slug=slugify(foodtitle)
            fooD.save()
            messages.success(request,'Food item  Updated  successfully!')
            return redirect('food_by_category' ,food.category.id)

    else:
        form=FooditmeForm(instance=food)


    context={
        'form':form,
        'food':food,
        'vendor':vendor
        
    }

    return render(request,'vendor/edit_food.html',context)

    



def delete_food(request,pk=None):
    food=get_object_or_404(FoodItem,pk=pk)
    food.delete()
    messages.success(request,'successfully delete !')
    return redirect('food_by_category' ,food.category.id)