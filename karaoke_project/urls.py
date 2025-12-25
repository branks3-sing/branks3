from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recorder.urls')),
]

# ✅ MEDIA + STATIC FILES - LOCAL + RENDER BOTH!
if settings.DEBUG or not os.environ.get('DATABASE_URL'):  # Local OR no DB URL
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
