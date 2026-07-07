from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    filename = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.image:
            self.filename = self.image.name.split("/")[-1]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.filename

class Polygon(models.Model):
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        related_name="polygons"
    )

    points = models.JSONField()
    label = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Polygon #{self.id} - {self.image.filename}"