from django.db import models
from django.conf import settings
import uuid as uuid_library
from core.models import TimeStampedModel


class Question(TimeStampedModel):
    class Meta:
        verbose_name = "Вопрос форума"
        verbose_name_plural = "Вопрос форума"
        ordering = ("-created_at", )

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=240, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="questions", on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True, serialize=False)

    def __str__(self):
        return self.title


class Answer(TimeStampedModel):
    class Meta:
        verbose_name = "Ответ форума"
        verbose_name_plural = "ответ на вопрос форума"
        ordering = ("id", "-updated_at",)

    # unique identifier, retrieve answer itself this will improve query speed
    uuid = models.UUIDField(db_index=True, editable=False, default=uuid_library.uuid4)
    body = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="answers", on_delete=models.DO_NOTHING)
    # every answer will liked by many and users will like a different answers
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.author.username