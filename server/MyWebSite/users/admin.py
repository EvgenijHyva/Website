from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

#admin.site.register(CustomUser)

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    readonly_fields = ("id",)
    list_display = ("username", "is_active", "age", "city")
