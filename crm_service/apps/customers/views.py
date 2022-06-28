from rest_framework import viewsets
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope

from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """

    permission_classes = [TokenHasReadWriteScope]

    queryset = Customer.objects.all().order_by("-date_joined")
    serializer_class = CustomerSerializer
