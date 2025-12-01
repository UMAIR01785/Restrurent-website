from django.db import models
from accounts.models import User,Userprofile
# Create your models here.
class Vendor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    user_profile=models.OneToOneField(Userprofile, on_delete=models.CASCADE)
    vendor_name=models.CharField( max_length=50)
    vendor_licience=models.ImageField( upload_to='vendor/licience')
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField( auto_now=True)


    def __str__(self):
        return self.vendor_name