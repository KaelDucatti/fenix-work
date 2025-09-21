from django.contrib import admin

from .models import CandidateProfile


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "social_name",
        "pronums",
        "bio",
        "resume",
        "linkedin",
        "github",
        "behance",
        "created_at",
        "updated_at",
    )
    search_fields = ("social_name", "user_id__username")
