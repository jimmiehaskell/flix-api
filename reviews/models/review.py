from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message='Avaliação não poder ser inferior a zero estrelas.'
            ),
            MaxValueValidator(
                limit_value=5,
                message='Avaliação não pode ser superior a 5 estrelas.'
            )
        ]
    )
    comment = models.TextField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.movie.title

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['rating']
        db_table = 'reviews'
