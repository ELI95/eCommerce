from django.contrib import admin

from .models import MarketingPreference


class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscribed', 'updated']
    readonly_fields = ['mailchimp_msg', 'mailchimp_subscribed', 'updated', 'timestamp']

    class Meta:
        model = MarketingPreference
        fields = [
                    'user',
                    'subscribed',
                    'mailchimp_msg',
                    'mailchimp_subscribed',
                    'updated',
                    'timestamp',
                ]


admin.site.register(MarketingPreference, MarketingPreferenceAdmin)
