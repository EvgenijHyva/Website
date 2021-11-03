from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from core.utils import from_cyrillic_to_slug

from forum.models import Question

@receiver(post_save, sender=Question)
def create_question_slug(sender, instance, *args, **kwargs):
    """when receiver is triggered on question it create slug"""
    if instance and not instance.slug:
        slug = from_cyrillic_to_slug(instance.title)
        random_string = get_random_string(length=6)
        instance.slug = slug + "_" + random_string
        instance.save()

