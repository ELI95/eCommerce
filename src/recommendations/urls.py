from django.conf.urls import url

from .views import user_based_recommendation


urlpatterns = [
    url(r'^user_based_cf/$', user_based_recommendation, name='home'),
]