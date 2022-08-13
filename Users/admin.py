from django.contrib import admin
from .models import User_Profile

@admin.register(User_Profile)
class User_Profile(admin.ModelAdmin):
    list_display = (
        'user',
        'phone_number',
        'image',
        'type_piece',
        'numero_piece',
        'image_piece_reto',
        'image_piece_verso',
        'Adresse',
        'type_user',
        'isactive'
    )

# Register your models here.
