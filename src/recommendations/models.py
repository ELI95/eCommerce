from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

from products.models import Product
from orders.models import ProductPurchase

from .custom_fileds import RatingField


class UserProductRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    product = models.ForeignKey(Product)
    rating = RatingField()
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s--%s' %(self.user, self.product)

    class Meta:
        ordering = ['timestamp']


def post_save_product_purchase_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProductRating.objects.create(
            user=instance.billing_profile.user,
            product=instance.product,
        )


post_save.connect(post_save_product_purchase_receiver, sender=ProductPurchase)
