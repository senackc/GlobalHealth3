from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class UserProfileClass(models.Model):
   
    IdentificicationNumber = models.CharField(max_length=15,null= True)
    PassportNumber = models.CharField(max_length=9,null= True)
    PhoneNumber = models.DecimalField(max_digits=1,decimal_places=0,null=True,)
    publications = models.ManyToManyField(User)


# Create your models here.
