from django.contrib import admin
from .models import savedLocations
# Register your models here.
class toDoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Item', {'fields': ['location']}),]
    list_display = ['location',]

admin.site.register(savedLocations, toDoAdmin)