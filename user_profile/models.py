




from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import json
from django.core import serializers
from django.http import JsonResponse



GENDER = [
        ('male', 'male'),
        ('female', 'female'),
        
    ]
class UserProfile(models.Model):
    # inital _mustl_need
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    profile_picture =models.CharField(max_length=255,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSooCX-nPSHN0kCVdUnm-eptCPvUF04YaxeHQ&s")
   # date_of_birth = models.DateField()
  
  #  gender = models.CharField(max_length=6, choices=GENDER,default='male')
    
    # presonal 
   # bio = models.TextField(max_length=500, blank=True)
   # website = models.URLField(blank=True)
   # phone_number = models.CharField(max_length=15, blank=True)
    #  user locaton  or address
    
   # country = models.CharField(max_length=50, blank=True, null=True,default="not set")
   # state = models.CharField(max_length=50, blank=True, null=True,default="not set")
   # city = models.CharField(max_length=50, blank=True, null=True,default="not set")
    
   
  #  is_profile_locked=models.BooleanField(default=False)
  
    
    
    