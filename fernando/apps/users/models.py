
from __future__ import unicode_literals
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.quotes.models import Quote
from apps.projects.models import Project







class User(AbstractBaseUser, PermissionsMixin):

    email        = models.EmailField(_('email address'), unique=True ,help_text='Introduce a valid email please')
    date_joined  = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active    = models.BooleanField(_('active'), default=True)
    is_admin     = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_client    = models.BooleanField(default=False,)
    is_visitor   = models.BooleanField(default=True,)
    is_employee  = models.BooleanField(default=False,)
    is_provider  = models.BooleanField(default=False,)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('Users')
        verbose_name_plural = _('users')


    def email_user(self, subject, message, from_email=None, **kwargs):
       
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Profile_Client(models.Model):
    company_name      = models.CharField(max_length=30, blank=True, default="Introduce company name")
    user              = models.OneToOneField(User, on_delete=models.CASCADE ,verbose_name="Email")
    physical_address  = models.CharField(max_length=200, blank=True)
    postal_address    = models.CharField(max_length=30, blank=True)
    phone             = models.CharField(max_length=30, blank=True)
    gst_registered    = models.BooleanField(default=True)
    company_director  = models.CharField(max_length=30, blank=True, default="Introduce company director")
    company_email     = models.EmailField(_('email address'),blank=True)
    
    def __str__(self):
        return    self.company_name
    

    
    

    class Meta:        
        verbose_name = "Client Profile"
        verbose_name_plural = "Client Profiles"


class Profile_Provider(models.Model):
    user              = models.OneToOneField(User, on_delete=models.CASCADE ,verbose_name="Email")
    company_name      = models.CharField(max_length=30, blank=True,default="Introduce company name")
    address           = models.CharField(max_length=200, blank=True)
    city              = models.CharField(max_length=30, blank=True)
    location          = models.CharField(max_length=30, blank=True)
    postal_Code       = models.CharField(max_length=4, blank=True)
    gst_registered    = models.BooleanField(default=True)
    company_director  = models.CharField(max_length=30, blank=True, default="Introduce company director")
    company_email     = models.EmailField(_('email address'),blank=True)
    contact_phone     = models.CharField(max_length=30, blank=True)
    contact_person1   = models.CharField(max_length=30, blank=True)
    contact_person1   = models.CharField(max_length=30, blank=True)
    contact_person2   = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return   self.company_name

    class Meta:        
        verbose_name = "Provider Profile"
        verbose_name_plural = "Provider Profiles"


class Profile_Employee(models.Model):
    user              = models.OneToOneField(User, on_delete=models.CASCADE ,verbose_name="Email")
    avatar            = models.ImageField(upload_to='avatars/', null=True, blank=True)
    employee_name     = models.CharField(max_length=30, blank=True, )
    employee_email    = models.EmailField(("email"),max_length=30, blank=True, default="email")
    position          = models.CharField(max_length=30, blank=True, default="position")
    hour_price_int    = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
    hour_price        = models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=10)
    start_date        = models.DateField(blank=True, null=True)
    address           = models.CharField(max_length=200, blank=True)
    city              = models.CharField(max_length=30, blank=True)
    location          = models.CharField(max_length=30, blank=True)
    postal_Code       = models.CharField(max_length=4, blank=True)


    class Meta:        
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"

    def __str__(self):
        return self.employee_name







@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    try:

        if instance.is_client: 
            if created:
                a=instance.email
                Profile_Client.objects.create(user=instance,company_email=a)
                
        elif instance.is_employee:
            if created:
                a=instance.email
                Profile_Employee.objects.create(user=instance,employee_email=a)

        elif instance.is_provider:
            if created:
                a=instance.email
                Profile_Provider.objects.create(user=instance,company_email=a)
        else:

            pass
    except :
        pass


@receiver(post_save, sender=User)
def save_user_profile(sender, instance,**kwargs):
    
    try:
        a=instance.email
        if instance.is_client:
            instance.profile_client.save()
            
    except :
        if instance.is_client:
            Profile_Client.objects.create(user=instance,company_email=a )

    try:
        a=instance.email
        if instance.is_employee:

            instance.profile_employee.save()
    except :
        if instance.is_employee:
            Profile_Employee.objects.create(user=instance,employee_email=a)  

    try:
        a=instance.email
        if instance.is_provider:
            instance.profile_provider.save()
    except :
        if instance.is_provider:
            Profile_Provider.objects.create(user=instance,company_email=a)    



    try:   
        if not instance.is_provider:
            instance.profile_provider.delete()
            
    except:
        pass

    try:   
        if not instance.is_employee:
            instance.profile_employee.delete()
            
    except:
        pass

    try:   
        if not instance.is_client:
            
            instance.profile_client.delete()
    except:
        pass

