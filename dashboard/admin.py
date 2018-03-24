from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.StartUps)
admin.site.register(models.Profile)
admin.site.register(models.Ventures)
admin.site.register(models.Ventures_Request)