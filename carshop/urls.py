"""
URL configuration for carshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from cars.views import home_view 
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('', include('cars.urls')),
]

# Only add these URL patterns if DEBUG is False and INSECURE_SERVE_STATIC_FILES_BY_DJANGO is True
# Or if DEBUG is True (though Django's dev server handles it then, this ensures consistency if INSECURE is also True)
if not settings.DEBUG and getattr(settings, 'INSECURE_SERVE_STATIC_FILES_BY_DJANGO', False):
    urlpatterns += [
        re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'), serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
        re_path(r'^%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'), serve, {  # Add this for static files
            'document_root': settings.STATIC_ROOT,
        }),
    ]
elif settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

