from django.db import models

class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("id", "-created_at",)

    name = models.CharField(max_length=50, blank=False, null=False, verbose_name="Название города")
    slug = models.CharField(max_length=50, blank=True, verbose_name="Слаг-поле")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    def __str__(self):
        return self.name

