import random
from django.db import models
from Users.models import User_Profile

class Colis(models.Model):
    users = models.ForeignKey(User_Profile, on_delete=models.CASCADE , related_name="colis_user")
    title_de_colis = models.CharField(max_length=255)
    type_colis = models.CharField(max_length=255)
    description_colis = models.TextField()
    code_colour_colis = models.CharField(max_length=255)
    package_colour_colis = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    status_payment = models.BooleanField(default=False)
    prix = models.DecimalField(max_digits=6 , decimal_places=3)
    adresse_livrasion = models.CharField(max_length=255)
    adresse_livrasion_latitude = models.CharField(max_length=255)
    adresse_livrasion_longitude = models.CharField(max_length=255)
    point_de_livraison = models.TextField()
    point_de_livraison_longitude = models.TextField()
    point_de_livraison_latitude = models.TextField()
    code_colis = models.CharField(max_length=255, default="", blank=True)
    nom_de_destination = models.TextField()
    current_position_latitude = models.TextField()
    current_position_longitude = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
    def generate_code(self):
        self.code_colis(random.radint(10000, 99999))
        
    def __str__(self):
        return str(self.users.user)
    
     

# Create your models here.
