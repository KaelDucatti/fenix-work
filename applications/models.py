from django.db import models

from accounts.models import CandidateProfile
from jobs.models import Job


class Application(models.Model):
    STATUS = [
        ("pending", "PENDENTE"),
        ("in_review", "EM ANÁLISE"),
        ("approved", "APROVADO"),
        ("rejected", "REPROVADO"),
        ("interview", "ENTREVISTA"),
    ]

    id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(
        CandidateProfile, on_delete=models.CASCADE, related_name="applications"
    )
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="applications"
    )
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS)

    def __str__(self):
        return (
            f"{self.candidate.social_name} → {self.job.title} ({self.status})"
        )

    class Meta:
        ordering = ["application_date"]
        verbose_name_plural = "Applications"
        constraints = [
            models.UniqueConstraint(
                fields=["candidate", "job"], name="unique_candidate_job"
            )
        ]
