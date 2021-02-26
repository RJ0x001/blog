from django.db import models
from django.conf import settings
from django.utils.timezone import now
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.TextField(max_length=50)
    text = models.TextField(max_length=1000, help_text="Введите текст.")
    created_time = models.DateField(default=now, editable=False)
    updated_time = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

