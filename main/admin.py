from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Category)
admin.site.register(models.Budget)
admin.site.register(models.Account)
admin.site.register(models.Total)
admin.site.register(models.Asset)
admin.site.register(models.Bill)