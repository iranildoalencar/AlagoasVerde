from django.db import models

class Doadores(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bairro = models.CharField(max_length=100)
    cidade   = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    d_nasc = models.DateField('Data de Nascimento')

    def __str__(self):
        return self.first_name + ' ' + self.last_name