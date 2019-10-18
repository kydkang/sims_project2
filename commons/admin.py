from django.contrib import admin
from .models import Description

# @admin.register(Post)     #  or, at the bottom
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('sequence', 'index_name', 'department')

admin.site.register(Description, DescriptionAdmin)  
