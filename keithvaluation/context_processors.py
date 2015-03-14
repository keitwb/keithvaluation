from django.conf import settings

def ga_account(request):
    return {'ga_account': settings.GA_ACCOUNT}
