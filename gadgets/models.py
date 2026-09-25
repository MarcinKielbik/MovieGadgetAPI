from django.db import models

class MovieGadget(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    movie = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    actor = models.CharField(max_length=150)
    character = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='gadgets/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title