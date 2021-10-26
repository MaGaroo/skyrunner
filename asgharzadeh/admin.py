from django.contrib import admin

from . import models


admin.site.register(models.Room)


@admin.register(models.NightName)
class NightNameAdmin(admin.ModelAdmin):
    fields = ('name', 'start', 'end')
