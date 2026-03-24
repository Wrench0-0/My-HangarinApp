#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin.settings')
django.setup()

from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models import Site

# Get the current site
site = Site.objects.get_current()

# Create Google OAuth app
google_app, created = SocialApp.objects.get_or_create(
    provider='google',
    defaults={
        'name': 'Google',
        'client_id': 'your-google-client-id',
        'secret': 'your-google-secret'
    }
)
if google_app not in site.socialapp_set.all():
    site.socialapp_set.add(google_app)
print(f'Google app: {"created" if created else "already exists"}')

# Create GitHub OAuth app
github_app, created = SocialApp.objects.get_or_create(
    provider='github',
    defaults={
        'name': 'GitHub',
        'client_id': 'your-github-client-id',
        'secret': 'your-github-secret'
    }
)
if github_app not in site.socialapp_set.all():
    site.socialapp_set.add(github_app)
print(f'GitHub app: {"created" if created else "already exists"}')

print('Social apps configured successfully!')
