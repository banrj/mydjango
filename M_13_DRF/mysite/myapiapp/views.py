from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from shopapp.models import Product, Order
from .serializers import ProductSerializer, OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({'message': 'Hello World!'})


class ProductViewSet(ModelViewSet):
    """
    НАбор представления для действий над Product
    full CRUD for model
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    filterset_fields = [
        'name', 'description', 'price'
    ]
    ordering_fields = [
        'name', 'description', 'price'

    ]


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        'delivery_address', 'promocode', 'created_at', 'user'
    ]
    ordering_fields = [
        'delivery_address', 'promocode', 'created_at', 'user'
    ]
