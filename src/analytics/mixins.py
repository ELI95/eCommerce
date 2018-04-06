from .signals import object_viewed_signal
from .models import ProductAnalytic


class ObjectViewedMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(ObjectViewedMixin, self).get_context_data(*args, **kwargs)
        request = self.request
        instance = context.get('object')
        if instance:
            product_analytic_qs = ProductAnalytic.objects.filter(product=instance)
            if product_analytic_qs.count() == 1:
                product_analytic_obj = product_analytic_qs.first()
                product_analytic_obj.viewed += 1
                product_analytic_obj.save()
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return context
