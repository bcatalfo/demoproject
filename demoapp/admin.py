from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Menu, MenuCategory

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)

# Unregister the provided model admin
admin.site.unregister(User)


@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        "date_joined",
    ]
