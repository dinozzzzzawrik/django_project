from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    content = models.CharField(blank=True, max_length=1000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ('-created_at',)

    def __str__(self):
        return self.title