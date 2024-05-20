from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group


class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'last_login',
        'date_joined',
        'is_active',
        'is_superadmin'
    )
    list_display_links = (
        'email',
        'first_name',
        'last_name'
    )
    readonly_fields = ('last_login', 'date_joined')
    ordering = ['-date_joined']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'phone_number', 'password1', 'password2')
        }),
    )

admin.site.register(Account, AccountAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)

