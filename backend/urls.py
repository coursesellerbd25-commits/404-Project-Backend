from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from accounts.views import EmailTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Task API
    path("api/", include("tasks.urls")),

    # Annotation API
    path("api/annotations/", include("annotations.urls")),

    # Auth
    path(
        "api/login/",
        EmailTokenObtainPairView.as_view(),
        name="login"
    ),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
]