from django.urls import path, include
from rest_framework.routers import DefaultRouter
from services import views

router = DefaultRouter()
router.register('service',views.ServiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]