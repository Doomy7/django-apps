from django.contrib import admin
from .models import toDoListItems

# Register your models here.
class toDoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Item', {'fields': ['listItem']}),
        ('Time Limit', {'fields': ['time_limit']}),
    ]
    list_display = ['listItem', 'time_limit']

admin.site.register(toDoListItems, toDoAdmin)