from django.db import models

# Create your models here.

class Usuarios (models.Model):

    usuario = models.CharField(max_length=15)
    email = models.EmailField()
    uids = models.IntegerField()
    server = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.usuario} --- {self.uids} --- {self.server}"
    
class e_adventure (models.Model):

    pj_nombre = models.CharField(max_length=15)
    pj_elemento = models.CharField(max_length=10)
    pj_lv = models.IntegerField()

    def __str__(self):
        return f"{self.pj_nombre} --- {self.pj_elemento} --- {self.pj_lv}"

    

class e_abiss (models.Model):

    pj_nombre = models.CharField(max_length=15)
    pj_elemento = models.CharField(max_length=10)
    pj_lv = models.IntegerField()
    fecha_abismo = models.DateField()
    paso = models.BooleanField()

    def __str__(self):
        return f"{self.pj_nombre} --- {self.pj_lv} --- {self.paso}"
