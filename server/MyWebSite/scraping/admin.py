from django.contrib import admin
from scraping.models import City
# Register your models here.

@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("id", "-created_at",)
    search_fields = ("name", "id")
    readonly_fields = ("created_at", "updated_at")

