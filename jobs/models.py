from django.db import models

from accounts.models import Enterprise


class Job(models.Model):
    MODALITIES = [
        ("presencial", "PRESENCIAL"),
        ("remoto", "REMOTO"),
        ("híbrido", "HÍBRIDO"),
    ]

    id = models.AutoField(primary_key=True)
    enterprise = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE, related_name="job"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    localization = models.CharField(max_length=255, blank=True, null=True)
    modality = models.CharField(max_length=20, choices=MODALITIES)
    wage = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.enterprise.name})"

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name_plural = "Jobs"
