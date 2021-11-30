from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from .utils import slugify_intance_title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    blog_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # return f'/blogs/{self.slug}/'
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


def blog_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_intance_title(instance, save=False)


pre_save.connect(blog_pre_save, sender=Blog)


def blog_post_save(sender, instance, created, *args, **kwargs):
    if created:
        slugify_intance_title(instance, save=True)


post_save.connect(blog_post_save, sender=Blog)
