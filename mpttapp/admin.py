from django.contrib import admin
from mpttapp.models import File
from mptt.admin import DraggableMPTTAdmin

# Register your models here.
admin.site.register(File, DraggableMPTTAdmin)