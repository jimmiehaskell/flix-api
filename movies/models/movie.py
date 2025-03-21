from django.db import models

from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    title = models.CharField(
        max_length=255
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies_fk'
    )
    release_date = models.DateField(
        null=True,
        blank=True
    )
    actors = models.ManyToManyField(
        Actor,
        related_name='movies_fk'
    )
    resume = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-release_date',]
        db_table = 'movies'
