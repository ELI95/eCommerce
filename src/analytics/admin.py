from django.contrib import admin

from .models import ProductAnalytic, ObjectViewed, UserSession


admin.site.register(ProductAnalytic)
admin.site.register(ObjectViewed)
admin.site.register(UserSession)
