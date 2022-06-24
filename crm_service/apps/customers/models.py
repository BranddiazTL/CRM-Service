from django.utils import timezone
from django.db import models

from base.models import UUIDModel
from base.utils.media_filename import handle_filename


class Customer(UUIDModel):
    ACTIVE = 'ACTIVE'
    DEACTIVATED = 'DEACTIVATED'
    SUSPENDED = 'SUSPENDED'

    status_choices = (
        (DEACTIVATED, DEACTIVATED),
        (SUSPENDED, SUSPENDED),
        (ACTIVE, ACTIVE),)

    image = models.ImageField('Image', upload_to=handle_filename, max_length=500, blank=False)
    email = models.EmailField('Email Address', unique=True, db_index=True)
    name = models.CharField('Name', unique=True, db_index=True, max_length=256, blank=False)
    surname = models.CharField('Surname', unique=True, db_index=True, max_length=256, blank=False)
    deactivated = models.DateTimeField('Deactivated', blank=True, null=True)
    status = models.CharField(
        'Customer Status', blank=True, null=True, choices=status_choices,
        max_length=20, default=ACTIVE)

    is_active = models.BooleanField('Active', default=True,
                                    help_text='Designates whether this customer should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('Date/Time Joined', default=timezone.now)
    created_by = models.CharField('Created by', blank=True, null=True, max_length=256)
    modified = models.DateTimeField('Modified', default=timezone.now)
    modified_by = models.CharField('Modified by', blank=True, null=True, max_length=256)
    last_changed_email = models.DateTimeField('Last changed email date', default=timezone.now)

    def __str__(self):
        return self.email
