# -*- coding: utf-8 -*-
from __future__ import (
    absolute_import,
    unicode_literals, )

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

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user.email

        if change:
            obj.modified_by = request.user.email

        super().save_model(request, obj, form, change)
