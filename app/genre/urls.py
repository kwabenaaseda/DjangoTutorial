from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.homepage, name='homepage'),
    
    # genre/ - This will now be at /genres/ (we'll keep both)
    path('genres/', views.index, name='genres_index'),
    
    # genre/collection/1
    path('genres/<int:collection_id>/', views.details, name='details'),
]