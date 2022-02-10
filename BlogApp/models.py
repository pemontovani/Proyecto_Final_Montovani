from django.db.models import  Model, ImageField, ForeignKey, CASCADE
from django.db.models.fields import (CharField, DateField)

from django.contrib.auth.models import User

# Create your models here. 
class Blog(Model):
    titulo= CharField(max_length=50)
    subtitulo= CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE)
    fecha= DateField()
    contenido= CharField(max_length=1000)
    imagen= ImageField(upload_to='imagenes', null=True, blank=True)
    
    class Meta:
       ordering = ['-fecha']
    
class Bio(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    biografia = CharField(max_length=1000)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)

