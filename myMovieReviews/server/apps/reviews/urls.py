from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviewsList),
    path('reviews-create', views.reviewsCreate),
    path('reviews-detail/<int:pk>', views.reviewsDetail),
    path('reviews-update/<int:pk>', views.reviewsUpdate),
    path('reviews-delete/<int:pk>', views.reviewsDelete)
]