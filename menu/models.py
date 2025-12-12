from django.db import models
from vendor.models import Vendor
# Create your models here


class Category(models.Model):
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_name=models.CharField( max_length=50)
    slug=models.SlugField()
    description=models.CharField( max_length=50)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'



    def __str__(self):
        return self.category_name
    
class FoodItem(models.Model):
    vendor=models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name=models.CharField( max_length=50)
    slug=models.SlugField()
    price=models.CharField( max_length=50)
    photo=models.ImageField( upload_to='fooditem' )
    is_available=models.BooleanField(default=True)
    description=models.CharField( max_length=50)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)


    


    def __str__(self):
        return self.item_name
    
