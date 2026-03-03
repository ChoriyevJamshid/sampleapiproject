
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.text import slugify


"""
Category: title, slug
Post: title, slug, summary, content, author, published_at, views, read_time, images

"""

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Nom")
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['created_at']


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique_for_date='published_at',
                            blank=True,
                            null=True)

    summary = models.CharField(max_length=511)
    content = models.TextField()

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='posts')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE,
                               related_name='posts')

    views = models.PositiveIntegerField(default=0)
    read_time = models.PositiveSmallIntegerField(default=0)

    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




