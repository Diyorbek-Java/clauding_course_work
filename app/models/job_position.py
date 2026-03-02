from django.db import models

class JobPosition(models.Model):
    """
    Job Position/Title model
    Examples: Senior Developer, Sales Manager, HR Coordinator, etc.
    """
    title = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True, help_text="Position description and responsibilities")

    is_active = models.BooleanField(default=True, help_text="Is this position currently available?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Job Positions'

    def __str__(self):
        return self.title