from django.contrib import admin
from django.urls import path, include
import posts.views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', posts.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls')),
    path('actualized/', posts.views.most, name='most'),
    path('mostvoted/', posts.views.latest, name='latest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
