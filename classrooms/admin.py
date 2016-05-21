from django.contrib import admin
from .models import Classroom


class ClassroomAdmin(admin.ModelAdmin):
    '''
        Admin View for Classroom
    '''
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Classroom, ClassroomAdmin)
