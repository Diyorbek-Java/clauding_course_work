from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ( 'full_name', 'role', 'department', 'position', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active', 'department', 'position')
    search_fields = ( 'full_name', 'phone_number')
    ordering = ('full_name',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name',  'phone_number')}),
        ('Job Info', {'fields': ('role', 'department', 'position', 'managed_organization')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'full_name',  'role', 'department', 'position', 'phone_number', 'is_staff', 'is_active')}
        ),
    )