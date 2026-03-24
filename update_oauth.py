#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin.settings')
django.setup()

from allauth.socialaccount.models import SocialApp

def update_oauth_credentials():
    print("Current OAuth credentials:")
    for app in SocialApp.objects.all():
        print(f"{app.provider.upper()}: {app.client_id[:20]}... (Status: {'Configured' if app.client_id and app.client_id != f'your-{app.provider}-client-id' else 'Placeholder'})")

    print("\n" + "="*50)
    print("UPDATE OAUTH CREDENTIALS")
    print("="*50)

    # Update Google
    try:
        google = SocialApp.objects.get(provider='google')
        print(f"\nCurrent Google Client ID: {google.client_id}")
        new_google_id = input("Enter your Google OAuth Client ID (or press Enter to skip): ").strip()
        if new_google_id:
            google.client_id = new_google_id
            new_google_secret = input("Enter your Google OAuth Client Secret: ").strip()
            if new_google_secret:
                google.secret = new_google_secret
                google.save()
                print("✅ Google OAuth updated successfully!")
            else:
                print("❌ Google secret not provided - update cancelled")
        else:
            print("Google update skipped")
    except SocialApp.DoesNotExist:
        print("❌ Google app not found")

    # Update GitHub
    try:
        github = SocialApp.objects.get(provider='github')
        print(f"\nCurrent GitHub Client ID: {github.client_id}")
        new_github_id = input("Enter your GitHub OAuth Client ID (or press Enter to skip): ").strip()
        if new_github_id:
            github.client_id = new_github_id
            new_github_secret = input("Enter your GitHub OAuth Client Secret: ").strip()
            if new_github_secret:
                github.secret = new_github_secret
                github.save()
                print("✅ GitHub OAuth updated successfully!")
            else:
                print("❌ GitHub secret not provided - update cancelled")
        else:
            print("GitHub update skipped")
    except SocialApp.DoesNotExist:
        print("❌ GitHub app not found")

    print("\n" + "="*50)
    print("FINAL STATUS")
    print("="*50)
    for app in SocialApp.objects.all():
        status = "✅ Configured" if app.client_id and app.client_id != f'your-{app.provider}-client-id' else "❌ Placeholder"
        print(f"{app.provider.upper()}: {status}")

if __name__ == "__main__":
    update_oauth_credentials()