from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="candidateprofile",
            old_name="user_id",
            new_name="user",
        ),
        migrations.RenameField(
            model_name="enterprise",
            old_name="user_id",
            new_name="user",
        ),
    ]
