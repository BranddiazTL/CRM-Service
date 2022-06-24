from __future__ import unicode_literals
from django import forms

from customers.models import Customer


class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(CustomerAdminForm, self).__init__(*args, **kwargs)
