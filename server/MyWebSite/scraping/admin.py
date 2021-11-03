from django.contrib import admin
from scraping.models import City, Language, Vacancy

@admin.register(City)
class AdminCity(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("id", "-created_at",)
    search_fields = ("name", "id")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Language)
class AdminLanguage(admin.ModelAdmin):
    list_display = ("id", "name")
    ordering = ("id", "-created_at",)
    search_fields = ("name", "id")
    readonly_fields = ("created_at",)

@admin.register(Vacancy)
class AdminVacancy(admin.ModelAdmin):
    list_display = ("company", "city", "title", "salary")
    ordering = ("-timestamp",)
    search_fields = ("city", "title", )
    readonly_fields = ("timestamp", )
