from django.conf import settings

from .models import FeatureFlag

def google_keys(request):
    return {
        'ga_account': settings.GA_ACCOUNT,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }

def feature_flags(request):
    flags = set(FeatureFlag.objects.filter(enabled=True).values_list('name', flat=True))

    for k, v in request.GET.items():
        if k.startswith("ff_"):
            name = k[3:]
            enabled = v != "false"
            if not enabled and name in flags:
                flags.remove(name)
            elif enabled:
                flags.add(name)

    return {
        'feature_flags': flags,
    }
