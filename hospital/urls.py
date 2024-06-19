from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('doctor/',include('doctor.urls')),
    # path('appointment/',include('appoitment.urls')),
    # path('patient/',include('patient.urls')),
    # path('contactus/',include('contactus.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)