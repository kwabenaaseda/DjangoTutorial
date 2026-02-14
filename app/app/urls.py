from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('genre.urls')),  # This makes homepage available at root
    path('genres/', include('genre.urls')),  # This keeps your existing genres URLs
    path('admin/', admin.site.urls),
]