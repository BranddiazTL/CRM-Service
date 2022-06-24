# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals, )
from collections import Counter

# Third Party Stuff
from customers.models import Customer
from customers.forms import CustomerAdminForm
from django.contrib import admin


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    form = CustomerAdminForm

    ordering = ('email',)

    readonly_fields = [
        'created_by', 'modified_by', 'date_joined', 'last_changed_email']

    def signed_up_from(self, obj):
        try:
            return Log.objects \
                .order_by('created') \
                .filter(
                    event=Log.EVENTS.CUSTOMER_SIGN_UP,
                    metadata__customer_id=str(obj.id)) \
                .first().metadata['application']

        except (AttributeError, KeyError):
            return 'unknown'

    def login_stats(self, obj):
        logs = Log.objects \
            .order_by('created') \
            .filter(
                event=Log.EVENTS.CUSTOMER_SIGN_IN,
                metadata__customer_id=str(obj.id))

        counter = Counter(map(
            lambda log: log.metadata.get('application', 'unknown'),
            logs))

        return ', '.join([': '.join(map(str, item)) for item in counter.items()])
