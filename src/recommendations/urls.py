from django.conf.urls import url

from .views import UserBasedRecommendationView, ItemBasedRecommendationView, UserItemRecommendationView


urlpatterns = [
    url(r'^user_based_cf/$', UserBasedRecommendationView.as_view(), name='user_based_cf'),
    url(r'^item_based_cf/$', ItemBasedRecommendationView.as_view(), name='item_based_cf'),
    url(r'^user_item_cf/$', UserItemRecommendationView.as_view(), name='user_item_cf'),
]