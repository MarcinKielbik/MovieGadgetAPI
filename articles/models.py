from django.db import models
from gadgets.models import MovieGadget


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='articles/',
        blank=False,
        null=False
    )
    content = models.TextField()

    gadget = models.ForeignKey(
        MovieGadget,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    def __str__(self):
        return self.title
