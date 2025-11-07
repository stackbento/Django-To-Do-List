from django.contrib import admin
from . models import List


# Register your models here.
#registering the model "List" created in models.py to access in the admin panel. 
admin.site.register(List)
