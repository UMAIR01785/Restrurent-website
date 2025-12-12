from django.contrib import admin
from . models import Category,FoodItem


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=('category_name','vendor','updated_at')
    search_fields=('category_name','vendor__vendor_name',)

class FooditemAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('item_name',)}
    list_display=('item_name','is_available','category','vendor','updated_at',)
    search_fields=('item_name','category__category_name','vendor__vendor_name',)
    list_filter=('is_available',)



admin.site.register(Category,CategoryAdmin)
admin.site.register(FoodItem,FooditemAdmin)
# Register your models here.
