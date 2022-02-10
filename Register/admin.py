from django.contrib import admin
from .models import Register
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list =('id','first_name','last_name','email','password')

admin.site.register(Register, RegisterAdmin)    