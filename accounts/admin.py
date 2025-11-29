from django.contrib import admin
from  . models import User ,Userprofile
from django.contrib.auth.admin import UserAdmin
class customAdmin(UserAdmin):
    list_display=['email','username','first_name','is_admin','is_active']
    list_display_links=['email','username']
    ordering=('-joined_date',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(User,customAdmin)
admin.site.register(Userprofile)
# Register your models here.
