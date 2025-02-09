from django.contrib import admin
from .models import Myuser
# Register your models here.


@admin.register(Myuser)
class Adminuser(admin.ModelAdmin):
    list_display = ['email','username','date_of_birth','last_name','first_name','date_joined','last_login','is_admin','is_active','is_staff','is_superuser']
    search_fields = ['email','username','date_of_birth','last_name','first_name']
    list_filter = ['email','username','date_of_birth','last_name','first_name']