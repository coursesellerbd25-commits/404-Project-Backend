from django.urls import path
from .views import (
    ImageUploadView,
    PolygonCreateView,
    PolygonListView,
    PolygonDeleteView,
)

urlpatterns = [
    # Upload image
    path("upload/", ImageUploadView.as_view(), name="image-upload"),

    # Create polygon
    path("polygon/", PolygonCreateView.as_view(), name="polygon-create"),

    # List polygons
    path("polygon/list/", PolygonListView.as_view(), name="polygon-list"),

    # Delete polygon
    path("polygon/<int:pk>/", PolygonDeleteView.as_view(), name="polygon-delete"),
]