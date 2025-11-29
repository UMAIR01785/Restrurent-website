from . models import User,Userprofile
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        Userprofile.objects.create(user=instance)
    else:
        try:
            profile=Userprofile.objects.get(user=instance)
            profile.save()
        except Userprofile.DoesNotExist:
            Userprofile.objects.create(user=instance)