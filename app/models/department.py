from django.db import models
from app.models.organization import Organization


class Department(models.Model):
    """
    Department/Team model
    Examples: Sales, Engineering, HR, Marketing, Finance, etc.
    """
    name = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True, help_text="Department description and responsibilities")
    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments',
        help_text="Organization this department belongs to"
    )
    head_of_department = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments_headed',
        help_text="Manager/Head of this department"
    )
    is_active = models.BooleanField(default=True, help_text="Is this department currently active?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name

