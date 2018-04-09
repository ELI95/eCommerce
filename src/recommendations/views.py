from django.views.generic import ListView

from .user_cf import UserBasedCF
from .item_cf import ItemBasedCF
from products.models import Product


class UserBasedRecommendationView(ListView):
    template_name = 'recommendations/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserBasedRecommendationView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        user = request.user
        user_based_cf = UserBasedCF()
        recommendations = user_based_cf.recommend(user)
        ids = [item[0] for item in recommendations]
        return Product.objects.filter(id__in=ids)


class ItemBasedRecommendationView(ListView):
    template_name = 'recommendations/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ItemBasedRecommendationView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        user = request.user
        item_based_cf = ItemBasedCF()
        recommendations = item_based_cf.recommend(user)
        ids = [item[0] for item in recommendations]
        return Product.objects.filter(id__in=ids)


class UserItemRecommendationView(ListView):
    template_name = 'recommendations/list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserItemRecommendationView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        user = request.user

        user_based_cf = UserBasedCF()
        user_based_recommendations = user_based_cf.recommend(user)
        user_based_ids = [item[0] for item in user_based_recommendations]

        item_based_cf = ItemBasedCF()
        item_based_recommendations = item_based_cf.recommend(user)
        item_based_ids = [item[0] for item in item_based_recommendations]

        ids = list(set(user_based_ids) | set(item_based_ids))
        return Product.objects.filter(id__in=ids)
