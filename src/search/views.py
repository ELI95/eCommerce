from itertools import chain

from django.shortcuts import render
from django.views.generic import ListView

from products.models import Product
from tags.models import Tag


class SearchProductView(ListView):
    template_name = 'search/view.html'
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        print(context)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            product_result = Product.objects.search(query)
            # tag_result = Tag.objects.search(query)

            queryset_chain = chain(
                product_result,
                # tag_result,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.viewed,
                        reverse=True)
            return qs
        return Product.objects.featured()
