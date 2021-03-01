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
    text = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if self.created_time:
            self.updated_time = now()
        super(Article, self).save(*args, **kwargs)
