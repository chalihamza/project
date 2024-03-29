from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pakweel import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('pages.urls')),
                  path('cars/', include('cars.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('contacts/', include('contacts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
