from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('username', 'first_name', 'last_name')
    fieldsets = (
        (None, {
            'fields': ('username', 'password', ('first_name', 'last_name'), 'email', 'classroom')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('is_active',),
        })
    )

admin.site.register(Student, StudentAdmin)
