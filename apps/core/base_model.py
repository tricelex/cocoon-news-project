from __future__ import annotations

from typing import Iterable

from django.db import models


class BaseAbstractModel(models.Model):

    """Base model for all models."""

    created_datetime = models.DateTimeField('Created at', auto_now_add=True)
    updated_datetime = models.DateTimeField('Last update at', auto_now=True)

    class Meta:
        abstract = True

    def save(
        self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = None,
        update_fields: Iterable[str] | None = None,
    ) -> None:
        """Override save method to set created_datetime and updated_datetime."""
        listed_for_update_fields = None
        if update_fields:
            listed_for_update_fields = list(update_fields)
            listed_for_update_fields.append('updated_datetime')
        return super().save(force_insert, force_update, using, listed_for_update_fields or None)
