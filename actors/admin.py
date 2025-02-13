from django.contrib import admin

from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name']
    ordering = ('-id',)
