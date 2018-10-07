from django.db import models


class Movie(models.Model):
    name = models.CharField('Nombre de la pelicula', max_length=30, blank=True, null=True)
    duration = models.FloatField("Duracion de la pelicula")
    description = models.TextField("Descripcion de la pelicula", max_length=300)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class User(models.Model):
    DNI = models.IntegerField('DNI', unique=True)
    email = models.EmailField('Correo electrónico', blank=False, null=False)
    password = models.CharField('Contraseña', max_length=20)
    name = models.CharField('Nombre', max_length=20, blank=True, null=True)
    last_name = models.CharField('Apellido', max_length=20, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.DNI, self.last_name)


class User_has_Movie(models.Model):
    User = models.ForeignKey(User, related_name='User_has_Movie', blank=True, null=True,
                             on_delete=models.SET_NULL)
    Movie = models.ForeignKey(Movie, related_name='User_has_Movie', blank=True, null=True,
                              on_delete=models.SET_NULL)
    price = models.IntegerField('Precio de la entrada', default=10)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.User.last_name, self.Movie.name)
