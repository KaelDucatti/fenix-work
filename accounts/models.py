from django.contrib.auth.models import User
from django.db import models


class CandidateProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cadidate_profiles"
    )
    social_name = models.CharField(max_length=200)
    pronums = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField()
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.social_name} ({self.pronums})"

    class Meta:
        ordering = ("social_name",)
        verbose_name_plural = "CadidateProfiles"


class Enterprise(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="enterprises"
    )
    name = models.CharField(max_length=200)
    site = models.URLField(blank=True, null=True)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Enterprises"
