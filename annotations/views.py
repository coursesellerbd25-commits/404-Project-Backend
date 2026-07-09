from rest_framework import generics, status
from rest_framework.response import Response
from .models import Image, Polygon
from .serializers import ImageSerializer, PolygonSerializer
import traceback

# Upload Image API
class ImageUploadView(generics.ListCreateAPIView):
    queryset = Image.objects.all().order_by("-id")
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(traceback.format_exc())
            return Response(
                {
                    "error": str(e),
                    "type": type(e).__name__,
                },
                status=500,
            )

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