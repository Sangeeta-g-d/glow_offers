from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=240, blank=True)
    image = models.ImageField(upload_to="offers/")
    link = models.URLField()
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-is_pinned", "-created_at"]

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Remove the image file from disk when the offer is deleted
        image = self.image
        super().delete(*args, **kwargs)
        if image:
            image.delete(save=False)
