import json
from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

ROLE_CHOICES = (
    ('superadmin'  , 'Super Admin'),
    ('admin'  , 'Admin'),
    ('user'  , 'User'),
)

# Create your models here.
class Daerah(models.Model):
    id_daerah    = models.AutoField(primary_key=True)
    nama_daerah  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_daerah
    
class Desa(models.Model):
    id_desa    = models.AutoField(primary_key=True)
    nama_desa  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_desa
    
class Kelompok(models.Model):
    id_kel    = models.AutoField(primary_key=True)
    nama_kel  = models.CharField(max_length = 100) 

    def __str__(self):
        return self.nama_kel

def avatar_with_id(instance, filename):
    return "{}/avatar/{}".format(f"{instance.user.id}", filename)

def convert_to_quill():
    converted_data = {
        "delta": "",
        "html": "Keterangan atau catatan dari data",
    }
    return json.dumps(converted_data)


class DataMas(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    role      = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    full_nama = models.CharField(max_length=255, null=True, blank=True)
    gender    = models.CharField(max_length=255, null=True, blank=True)
    no_hp     = models.CharField(max_length=255, null=True, blank=True)
    email     = models.CharField(max_length=255, null=True, blank=True)
    foto      = models.ImageField(upload_to=avatar_with_id, null=True, blank=True)
    keterangan       = QuillField(default=convert_to_quill())


    def __str__(self):
        return self.user.username