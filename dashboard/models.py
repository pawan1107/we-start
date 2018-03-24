from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StartUps(models.Model):
   start_up_name = models.CharField(max_length=256)
   start_up_description = models.TextField(blank=True, null=True)
   start_up_members = models.TextField(blank=True, null=True)
   start_up_skills_req = models.TextField(blank=True, null=True)
   start_up_sal = models.IntegerField()


   def __str__(self):
       return self.start_up_name


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   current_stratup = models.TextField(blank=True, null=True)
   applied_startup = models.TextField(blank=True, null=True)
   mobile = models.IntegerField()
   address = models.TextField(blank=True, null=True)


class Ventures(models.Model):
   ventures_name = models.TextField(blank=True, null=True)
   ventures_description = models.TextField(blank=True, null=True)


class Ventures_Request(models.Model):
   ventures_request_start_up_name = models.TextField(blank=True, null=True)
   ventures_request_USP = models.TextField(blank=True, null=True)
   ventures_request_Amount = models.IntegerField()