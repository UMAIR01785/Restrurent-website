from django.db import models
from accounts.models import User,Userprofile
from accounts.utils import send_verfication_mail
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
    

    def save(self):
        if self.pk is not None:
            orig=Vendor.objects.get(pk=self.pk)
            if orig.is_active != self.is_active:
                mail_template='accounts/send_verfication_email.html'
                context={
                    'user': self.user,
                    'is_active':self.is_active
                }
                if self.is_active:
                    mail_subject="Congrulation you are active to open the shop!"
                    send_verfication_mail(mail_subject,mail_template,context)
                else:
                    mail_subject="We are sorry to open the shop here please try again "
                    send_verfication_mail(mail_subject,mail_template,context)
        return super(Vendor,self).save()