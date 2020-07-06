from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal data information', {'fields': ['first_name', 'last_name']}),
        ('Permission data information', {'fields': ['role']}),
    ]
    list_display = ['full_name', 'role']
    list_filter = ['role']
    search_fields = ['first_name', 'last_name']


admin.site.register(Person, PersonAdmin)
