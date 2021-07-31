from django.db import models


# Create your models here.
class PageContent(models.Model):
    class Meta:
        verbose_name = "Главная - контент"
        verbose_name_plural = "Главная - контент"

    title = models.CharField(max_length=120, default="Default Title")
    image = models.ImageField(upload_to="mainPhoto", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
