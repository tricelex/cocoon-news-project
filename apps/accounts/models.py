import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.base_model import BaseAbstractModel


class User(AbstractUser):
    user_uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return f'{self.username} - {self.user_uuid}'

    def get_full_name(self) -> str:
        return super().get_full_name()


class Author(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    name = models.CharField(_("Name of Author"), blank=True, null=True, max_length=255)
    surname = models.CharField(_("Surname of Author"), blank=True, null=True, max_length=255)
    job_description = models.CharField(max_length=525, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
