from django.db import models

class Administrator(models.Model):
    DNI = models.IntegerField('DNI', unique=True)
    Name = models.CharField('Nombre', max_length=20)
    Last_Name = models.CharField('Apellido', max_length=20)
    Email = models.EmailField('Correo electrónico', blank=False, null=False)
    Password = models.CharField('Contraseña', max_length=20, blank=False, null=False)

    def __str__(self):
        return "{} - {}".format(self.DNI, self.Last_Name)