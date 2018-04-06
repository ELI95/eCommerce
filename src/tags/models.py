from django.db import models
from django.db.models.signals import pre_save, post_save
from django.db.models import Q

from products.models import Product
from ecommerce.utils import unique_slug_generator


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
        return self.filter(lookups).distinct()


class TagManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def search(self, query):
        return self.get_queryset().active().search(query)


class Tag(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    objects = TagManager()


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
