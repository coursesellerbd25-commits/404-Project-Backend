from rest_framework import serializers
from .models import Image, Polygon


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["id", "image", "filename", "uploaded_at"]

    def get_image(self, obj):
        return obj.image.url if obj.image else None


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = "__all__"