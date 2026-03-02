from django.contrib import admin
from .models.department import Department  
from .models.job_position import JobPosition
from .models.organization import Organization


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'head_of_department', 'is_active', 'created_at')
    list_filter = ('is_active', 'organization')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_organization', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')