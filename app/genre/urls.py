from django.urls import path
from . import views
urlpatterns = [
    # genre/
  path('', views.index, name='index'), 

  # genre/collection/1 
  path('<int:collection_id>/', views.details, name='details'),
]
