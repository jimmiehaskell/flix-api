import datetime

from django.contrib import admin

from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date']
    list_filter = ['id', 'release_date']
    ordering = ('-release_date',)
