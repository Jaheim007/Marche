from django.contrib import admin
from .models import Tracking

@admin.register(Tracking)
class Tracking(admin.ModelAdmin):
    list_display = (
        'users', 
        'current_position_details', 
        'current_position_longitude',
        'current_position_latitude',
        
    )

# Register your models here.
