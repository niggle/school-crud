from django.contrib import admin
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    '''
        Admin View for School
    '''
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(School, SchoolAdmin)
