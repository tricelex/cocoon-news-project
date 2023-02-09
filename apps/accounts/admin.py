from django.contrib import admin

from apps.accounts.models import Author, User

# Register your models here.
admin.site.register(User)
admin.site.register(Author)
