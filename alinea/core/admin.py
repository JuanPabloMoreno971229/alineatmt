from django.contrib import admin
from .models import CaruselLanding, Contact, what, how, logos, Project, Image

# Register your models here.
class LandingAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    readonly_fields = ('title','image_title')
    
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'mail', 'phone', 'message', 'created')
    list_filter = ('created', 'status')
    list_display = ('name', 'status')
   
class WhatAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')

class HowAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')
    
class LogosAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')
    
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')



admin.site.register(CaruselLanding, LandingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(what, WhatAdmin)
admin.site.register(how, HowAdmin)
admin.site.register(logos, LogosAdmin)
admin.site.register(Project, ProjectAdmin) 
admin.site.register(Image)