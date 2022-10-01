from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name='Categorie'
        
    def __str__(self):
        return self.nome    

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='título')
    content = models.TextField(verbose_name='corpo do artigo')
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='sub título')
    user = models.ForeignKey(User, on_delete = models.PROTECT, verbose_name='autor')

    class Meta:
        verbose_name = 'Artigo'
    
    def __str__(self):
        return self.title    
