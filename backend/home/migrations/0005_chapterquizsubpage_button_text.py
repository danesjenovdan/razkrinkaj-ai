# Generated by Django 5.0.9 on 2024-11-15 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_alter_chapterquizsubpage_answers"),
    ]

    operations = [
        migrations.AddField(
            model_name="chapterquizsubpage",
            name="button_text",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Besedilo gumba"
            ),
        ),
    ]
