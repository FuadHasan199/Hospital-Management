from django.contrib import admin
from .models import Specialization,Designation,AvailableTime,Doctor,Review

class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(Specialization,SpecializationAdmin)

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',),}

admin.site.register(Designation,DesignationAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)
admin.site.register(Review)