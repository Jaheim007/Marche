from django.contrib import admin
from .models import Colis

@admin.register(Colis)
class Colis(admin.ModelAdmin):
    list_display = (
        'users',
        'title_de_colis',
        'type_colis',
        'description_colis',
        'code_colour_colis',
        'package_colour_colis',
        'quantity',
        'status_payment',
        'prix',
        'adresse_livrasion',
        'adresse_livrasion_latitude',
        'adresse_livrasion_longitude',
        'point_de_livraison',
        'point_de_livraison_longitude',
        'point_de_livraison_latitude',
        'code_colis',
        'nom_de_destination',
        'current_position_latitude',
        'current_position_longitude'
    )

# Register your models here.
