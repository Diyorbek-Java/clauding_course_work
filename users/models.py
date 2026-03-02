from django.db import models
from app.models.department import Department
from app.models.job_position import JobPosition 
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):

    # Role choices
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    EMPLOYEE = 'EMPLOYEE'
    ORG_MANAGER = 'ORG_MANAGER'
    ORG_ADMIN = 'ORG_ADMIN'

    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee'),
        (ORG_MANAGER, 'Organization Manager'),
        (ORG_ADMIN, 'Organization Admin'),
    ]

    # User role and employee details
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    full_name = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees',
        help_text="Employee's department"
    )
    position = models.ForeignKey(
        JobPosition,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees',
        help_text="Employee's job position"
    )
    managed_organization = models.ForeignKey(
        'app.Organization',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='admin_users',
        help_text="Organization this user administers (only for ADMINISTRATION role)"
    )
    phone_regex = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Phone number must be entered in the format: '+998111111111'."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=13,  # +998 + 9 digits = 13 characters
        unique=True,
        blank=True,
        null=True,
        help_text="Employee phone number in format +998111111111"
    )

    class Meta:
        ordering = ['full_name']
        indexes = [
            models.Index(fields=['role']),
        ]

    def __str__(self):
        return f"{self.full_name} ({self.username})"
