from django.db import models


class User(models.Model):
    DNI = models.IntegerField('DNI', primary_key=True)
    email = models.EmailField('Correo electrónico', blank=False, null=False)
    password = models.CharField('Contraseña', max_length=20)
    name = models.CharField('Nombre', max_length=20, blank=True, null=True)
    last_name = models.CharField('Apellido', max_length=20, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.DNI, self.last_name)


class Movie(models.Model):
    name = models.CharField('Nombre de la pelicula', max_length=30, blank=True, null=True)
    duration = models.FloatField("Duracion de la pelicula")
    description = models.TextField("Descripcion de la pelicula", max_length=300)
    date = models.CharField("Estreno de la pelicula", max_length=30, blank=True, null=True)
    photo = models.ImageField("Foto de la pelicula", upload_to='movies', blank=True, null=True)
    clients = models.ManyToManyField(User, through='User_has_Movie')

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class User_has_Movie(models.Model):
    User = models.ForeignKey(User, related_name='User_has_Movie', blank=True, null=True,
                             on_delete=models.CASCADE)
    Movie = models.ForeignKey(Movie, related_name='User_has_Movie', blank=True, null=True,
                              on_delete=models.CASCADE)
    price = models.IntegerField('Precio de la entrada', default=10)
    date = models.CharField('Fecha de la compra', max_length=30, blank=True, null=True)
    time = models.CharField('Hora de la función', max_length=10, blank=True, null=True)
    place = models.CharField('Lugar de la función', max_length=30, blank=True, null=True)
    room_cinema = models.CharField('Sala de la función', max_length=10, blank=True, null=True)

    def __str__(self):
        return '{} - {} - {}'.format(self.id, self.User.last_name, self.Movie.name)
