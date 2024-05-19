from django.contrib import admin

# Register your models here.

from .models import *

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'image_display')

    def image_display(self, obj):
        return obj.image.url if obj.image else None

admin.site.register(Details, YourModelAdmin)