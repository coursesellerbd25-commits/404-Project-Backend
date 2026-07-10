from rest_framework import serializers
from .models import Image, Polygon


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.image:
            data["image"] = instance.image.url

        return data


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = "__all__"