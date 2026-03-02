from django.db import models

class Organization(models.Model):
    """
    Top-level organization entity.
    An organization has a head (one user) and contains multiple departments.
    """
    name = models.CharField(max_length=200, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    head_of_organization = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='organizations_headed',
        help_text="Head / CEO of this organization"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Organizations'

    def __str__(self):
        return self.name


