from django.urls import path

from . import views

urlpatterns = [
    path("", views.review),
    path("submit-success", views.ReviewView.as_view())
]
