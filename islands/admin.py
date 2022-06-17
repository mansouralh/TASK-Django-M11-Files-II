from django.contrib import admin

from islands import models

to_register = [
    models.IslandPhoto,
    models.Island,
]

admin.site.register(to_register)
