from customers.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "image",
            "email",
            "name",
            "surname",
            "deactivated",
            "status",
            "is_active",
        ]
