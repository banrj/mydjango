from django.urls import path, include
from .views import hello_world_view, ProductViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter


app_name = "myapiapp"

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('', include(router.urls))
]
