from django.db.models import  Model, ImageField, ForeignKey, CASCADE, OneToOneField
from django.db.models.fields import (CharField, DateField,TextField)
from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here. 
class Blog(Model):
    titulo= CharField(max_length=50)
    subtitulo= CharField(max_length=50)
    user = ForeignKey(User, on_delete=CASCADE)
    fecha= DateField()
    contenido= RichTextField()
    imagen= ImageField(upload_to='imagenes', null=True, blank=False)
    
    class Meta:
       ordering = ['-fecha']
    
class Bio(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    biografia = TextField()

    
def create_user_profile(sender, instance, created, **kwargs): 
    if created: profile, created = Bio.objects.get_or_create(user=instance)
post_save.connect(create_user_profile, sender=User)


