from django.contrib import admin
from mainpage.models import PageContent, Contacts


# Register your models here.

# admin.site.register(PageContent)
@admin.register(PageContent)
class AdminPageContent(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "created_at")
    fields = (("title", "created_at"), "home", ("image", "show_image"), "about", "updated_at",)
    ordering = ("created_at",)
    search_fields = ("title",)


admin.site.register(Contacts)
