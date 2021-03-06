# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals,
)

# Standard Library
import uuid

# Third Party Stuff
from django.db import models
from django.utils.translation import gettext_lazy as _


class UUIDModel(models.Model):
    """
    An abstract base class model that makes primary key `id` as UUID
    instead of default auto incremented number.
    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    @classmethod
    def subscribe_on_save(cls, condition):
        if not hasattr(cls, "_on_save_listeners"):
            setattr(cls, "_on_save_listeners", [])

        def wrapper(function):
            cls._on_save_listeners.append(
                {"condition": condition, "function": function}
            )

            return function

        return wrapper

    @classmethod
    def subscribe_on_create(cls):
        if not hasattr(cls, "_on_create_listeners"):
            setattr(cls, "_on_create_listeners", [])

        def wrapper(function):
            cls._on_create_listeners.append({"function": function})

            return function

        return wrapper

    def save(self, *args, **kwargs):
        cls = type(self)
        prev_state = cls.objects.filter(id=self.id).first()
        super().save(*args, **kwargs)

        if hasattr(cls, "_on_create_listeners") and not prev_state:
            for listener in cls._on_create_listeners:
                listener["function"](self)

        if hasattr(cls, "_on_save_listeners") and prev_state:
            for listener in filter(
                lambda listener: listener["condition"](prev_state, self),
                cls._on_save_listeners,
            ):
                listener["function"](prev_state, self)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields
    """

    created = models.DateTimeField(
        _("date/time created"), auto_now_add=True, editable=False
    )
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel, TimeStampedModel):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields with UUID as primary_key field.
    """

    class Meta:
        abstract = True
