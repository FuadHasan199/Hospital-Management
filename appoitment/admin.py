from django.contrib import admin
from appoitment.models import Appointment
# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['Doctor_name','Patient_name','appointment_types','appointment_status','status','time']

    def Patient_name(self,obj):
        return obj.patient.user.first_name
    
    def Doctor_name(self,obj):
        return obj.doctor.user.first_name
    
admin.site.register(Appointment,AppointmentAdmin)
    
    
