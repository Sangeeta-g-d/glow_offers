from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("django-admin/", admin.site.urls),  # Django's built-in admin (optional)
    path("", include("offers.urls")),
]

# Serve uploaded images while developing
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
