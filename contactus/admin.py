from django.contrib import admin
from .models import Contactus
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number','problem']

admin.site.register(Contactus,ContactModelAdmin)