from django.contrib import admin
from mainpage.models import PageContent, Contacts, PageSettings

# Register your models here.

# admin.site.register(PageContent)
@admin.register(PageContent)
class AdminPageContent(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "created_at", "id")
    fields = (("title", "created_at"), "home", ("image", "show_image"), "about", "updated_at",)
    ordering = ("-created_at",)
    search_fields = ("title",)

@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-pk", )
    search_fields = ("pk", "updated_at")


@admin.register(PageSettings)
class AdminPageSettings(admin.ModelAdmin):
    readonly_fields = ("modified_at", )
    list_display = ("user", "modified_at", "user_id")
    ordering = ("user_id", "modified_at")
    search_fields = ("user_id", )
    fields = ("user", "dark", "modified_at", ("addition_code", "insert_addition_code"))