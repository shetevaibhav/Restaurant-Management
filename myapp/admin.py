from django.contrib import admin
from .models import Receipe

# Register your models here.

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
     list_display = ["receipe_name", "receipe_description", "receipe_image"]

