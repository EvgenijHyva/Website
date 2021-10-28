from django.contrib import admin
from forum.models import Answer, Question

@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display = ("title", "author", "id", )
    ordering = ("id", "-created_at",)
    search_fields = ("slug", "id")
    readonly_fields = ("created_at", "updated_at")

@admin.register(Answer)
class AdminAnswer(admin.ModelAdmin):
    list_display = ("question", "author", "uuid",  "is_active", "id")
    ordering = ("id", "-created_at",)
    search_fields = ("question", "author", "id" )
    readonly_fields = ("created_at", "updated_at", "uuid")