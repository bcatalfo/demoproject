from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Menu, MenuCategory, Person

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)

# Unregister the provided model admin
admin.site.unregister(User)


@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if not request.user.is_superuser:
            form.base_fields["username"].disabled = True

        return form

    readonly_fields = [
        "date_joined",
    ]


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("Person_name", "age")
    search_fields = ("Person_name__startswith",)
