
from django.urls import path,include
from appoitment import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('',views.AppointmentViewSet)
urlpatterns = [
    path('api/',include(router.urls)),

]
