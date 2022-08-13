import random
from django.db import models
from django.contrib.auth.models import User

class User_Profile(models.Model):
    ADMIN = 'AD'
    VENDEUR = 'V'
    LIVREUR = 'L'
    CLIENT = "C"
    
    PASSEPORT = "PA"
    CARTEDIDENTITE = "CI"
    
    USER_TYPE = [
        (ADMIN,'Admin'),
        (VENDEUR,'Vendeur'),
        (LIVREUR,'Livreur'),
        (CLIENT ,'Client' )
    ]
    
    TYPE_DE_PIECE = [
        (PASSEPORT , 'Passeport'), 
        (CARTEDIDENTITE , "Carte D'identité")
    ]
    
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    image = models.ImageField(upload_to = "Image Profile")
    type_piece = models.CharField(choices=TYPE_DE_PIECE , max_length=255)
    numero_piece = models.PositiveIntegerField()
    image_piece_reto = models.ImageField(upload_to = "Image Reto")
    image_piece_verso = models.ImageField(upload_to = "Image Verso")
    Adresse = models.CharField(max_length=255)
    type_user  = models.CharField(choices=USER_TYPE , max_length=255)
    isactive = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
        
    def __str__(self):
        return str(self.user)
    
    
    
    
    
    