# Generated by Django 5.0.9 on 2024-12-19 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_finishedchapterdata_attempt_guid_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="pageanswerdata",
            name="answer_text",
            field=models.TextField(blank=True, verbose_name="Besedilo odgovora"),
        ),
    ]
