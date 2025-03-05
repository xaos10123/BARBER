from django.contrib import admin

from main.models import Master, Service, Visit

@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    pass

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
