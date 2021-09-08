from django.db import models

from users.models import CustomUser


class PageContent(models.Model):
    class Meta:
        verbose_name = "контент на страницу главная"
        verbose_name_plural = "Главная (контент страницы)"
        ordering = ("-created_at",)

    title = models.CharField(max_length=120, default="Default Title", verbose_name="Заголовок")
    home = models.TextField(blank=True, verbose_name="Home")
    image = models.ImageField(upload_to="MainPhoto", blank=True, verbose_name="фото/картинка")
    show_image = models.BooleanField(default=True)
    about = models.TextField(blank=True, verbose_name="about")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    def __str__(self):
        return f"{self.title} | created at: {self.created_at}"


class Contacts(models.Model):
    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
        ordering = ("-created_at",)

    github = models.CharField(max_length=256, unique=True, verbose_name="Сылка на Гитхаб",
                              blank=True, null=True, default=None)
    vk = models.CharField(max_length=256, unique=True, verbose_name="Сылка на vk",
                          blank=True, null=True, default=None)
    facebook = models.CharField(max_length=256, unique=True, verbose_name="Сылка на facebook",
                                blank=True, null=True, default=None)
    instagram = models.CharField(max_length=256, unique=True, verbose_name="Сылка на instagram",
                                 blank=True, null=True, default=None)
    telegram_username = models.CharField(max_length=256, unique=True,
                                verbose_name="имя пользователя для Телеграм", blank=True, null=True, default=None)
    whatsapp = models.CharField(max_length=256, unique=True, verbose_name="Телефон для whatsapp",
                                blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата обновления")

    def __str__(self):
        return f"контакты соц. сетей"


class PageSettings(models.Model):
    class Meta:
        verbose_name = "Настройки страницы"
        verbose_name_plural = "Настройки страницы"
        ordering = ("modified_at", "dark",)

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь",
                                related_name="user_settings", db_index=True,
                                primary_key=True)  # primary_key use only users pk
    dark = models.BooleanField(default=False, verbose_name="Ночной режим")
    background = models.CharField(verbose_name="Background", max_length=128, blank=True)
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Дата Обновления")
    addition_code = models.TextField(blank=True, verbose_name="Доп. код")
    insert_addition_code = models.BooleanField(default=False, verbose_name="добавить код")

