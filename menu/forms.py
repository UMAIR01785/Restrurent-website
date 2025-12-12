from django import forms
from .models import Category,FoodItem

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category_name','description']
        

class FooditmeForm(forms.ModelForm):
    class Meta:
        model=FoodItem
        fields=['category','item_name','price','is_available','photo','description']