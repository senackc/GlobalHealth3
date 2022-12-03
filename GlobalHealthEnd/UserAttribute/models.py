from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL



class UserAttributeClass(models.Model):
   
    HeightInfo = models.DecimalField(max_digits=4,decimal_places=2,null=True,)
    WeightIngo = models.DecimalField(max_digits=3,decimal_places=0,null=True,)
    AgeInfo = models.DecimalField(max_digits=2,decimal_places=0,null=True,)
    GenderInfo = models.BooleanField
    BloodGroupInfo = models.CharField(max_length=3,null= True)

    publications = models.ManyToManyField(User)





# Create your models here.
