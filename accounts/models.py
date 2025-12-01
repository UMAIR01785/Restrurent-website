from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class Myaccount(BaseUserManager):
    def create_user(self,first_name,last_name,email,username,password=None):
        if not email:
            raise ValueError("Email is not found")
        if not username:
            raise ValueError("Username is not found!")
        

        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,first_name,last_name,email,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_active=True
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user





class User(AbstractBaseUser):
    Customer=1
    Restaurant=2
    role_choices=(
        (1, 'customer'),
        (2, 'restaurant'),
    )
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField(unique=True, max_length=254)
    phone_number=models.CharField(blank=True,null=True)
    username=models.CharField(unique=True, max_length=50)
    role=models.IntegerField(choices=role_choices,null=True,blank=True)

    joined_date=models.DateTimeField(  auto_now_add=True)
    last_login=models.DateTimeField( auto_now=True)
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username',]


    objects=Myaccount()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
     return True
    

    def get_role(self):
        if self.role == 1:
            user_role='customer'
        elif self.role == 2:
            user_role = 'restaurant'
        return user_role
        

       




class Userprofile(models.Model):
   

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField( upload_to='user/profile_pic')
    cover_pic=models.ImageField( upload_to='user/cover_pic')
    address1=models.CharField( max_length=50)
    address2=models.CharField( max_length=50,null=True , blank=True)
    country=models.CharField( max_length=50)
    state=models.CharField( max_length=50)
    pin_code=models.CharField(max_length=5 ,null=True,blank=True)
    created_at=models.DateTimeField(  auto_now_add=True)
    modifed_at=models.DateTimeField( auto_now=True)
    


    def __str__(self):
        return f'{self.user.username}'
