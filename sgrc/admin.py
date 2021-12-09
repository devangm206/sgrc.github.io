from django.contrib import admin
from .models import studentgriev , contactus , facgrieve
# Register your models here.

admin.site.site_header = "Nhitm-SGRC"

class studentgrievAdmin(admin.ModelAdmin):
    list_display = ["name","contactnum","email","grievance","date_time","status"]


class contactusAdmin(admin.ModelAdmin):
    list_display = ["ctname","ctemail","ctsubject","ctmessage"]  

class facgrieveAdmin(admin.ModelAdmin):
    list_display = ["solution"]

admin.site.register(studentgriev,studentgrievAdmin),
admin.site.register(contactus,contactusAdmin),
admin.site.register(facgrieve,facgrieveAdmin)
