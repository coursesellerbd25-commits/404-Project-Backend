from rest_framework import generics
from .models import Image, Polygon
from .serializers import ImageSerializer, PolygonSerializer


# Upload Image API
class ImageUploadView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class PolygonCreateView(generics.CreateAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

class PolygonListView(generics.ListAPIView):
    serializer_class = PolygonSerializer

    def get_queryset(self):
        image_id = self.request.query_params.get("image")
        return Polygon.objects.filter(image_id=image_id)

class PolygonDeleteView(generics.DestroyAPIView):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer