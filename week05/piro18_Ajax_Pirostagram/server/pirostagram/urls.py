from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('create-comment/', views.create_comment),
    path('delete-comment/', views.delete_comment),
    path('toggle-like/', views.toggle_like),
]
