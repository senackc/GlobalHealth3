from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


class UserAllergenClass(models.Model):
   
    AllergenImportant = models.DecimalField(max_digits=1,decimal_places=0,null=True,)
    AllergenName = models.CharField(max_length=100,null= True)
    publications = models.ManyToManyField(User)


# Create your models here.
