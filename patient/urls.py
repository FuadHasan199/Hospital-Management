from django.urls import path,include
from rest_framework.routers import DefaultRouter
from patient import views

router = DefaultRouter()
router.register('patient',views.PatientViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]