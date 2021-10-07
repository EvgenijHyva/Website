from django.db import models
from scraping.utils import from_cyrillic_to_slug


class City(models.Model):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("id", "-created_at",)

    name = models.CharField(max_length=50, blank=False, null=False,
                            verbose_name="Название города", unique=True)
    slug = models.CharField(max_length=50, blank=True, verbose_name="Слаг-поле",
                            unique=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="дата обновления")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_slug(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    class Meta:
        verbose_name = "Язык програмирования"
        verbose_name_plural = "Языки програмирования"

    name = models.CharField(max_length=50, verbose_name="язык програмирования")
    slug = models.CharField(max_length=50, verbose_name="Слаг-поле", unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_slug(str(self.name))
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    class Meta:
        verbose_name = "Вакансию"
        verbose_name_plural = "Вакансии"

    url = models.URLField(null=False, blank=False, unique=True, verbose_name="Url вакансии")
    title = models.CharField(max_length=250, verbose_name="Должность")
    company = models.CharField(max_length=250, verbose_name="Компания")
    description = models.TextField(verbose_name="Описание дожности")
    salary = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Зарплата")
    city = models.ForeignKey("City", on_delete=models.CASCADE, verbose_name="Город")
    language = models.ForeignKey("Language", on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name="Язык програмирования", default=None)
    timestamp = models.DateField(auto_now_add=True, verbose_name="дата создания")

    def __str__(self):
        return f"{self.company}: {self.title} - {self.salary}"
