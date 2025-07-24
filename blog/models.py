
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image = models.ImageField(verbose_name="<UNK>", upload_to="post_images/", null=True, blank=True)

    def __str__(self):
        return self.title
