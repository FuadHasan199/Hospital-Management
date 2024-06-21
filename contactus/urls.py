from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contactus import views

router = DefaultRouter()
router.register(r'contactus', views.ContactUsViewSet,basename='contactus')


urlpatterns = [
    path('api/', include(router.urls)),
]