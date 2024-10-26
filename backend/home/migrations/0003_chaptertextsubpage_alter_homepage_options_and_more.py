# Generated by Django 5.0.9 on 2024-10-22 15:22

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
        ("wagtailcore", "0094_alter_page_locale"),
        ("wagtailimages", "0026_delete_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChapterTextSubPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "text",
                    wagtail.fields.RichTextField(blank=True, verbose_name="Besedilo"),
                ),
                (
                    "button_text",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Besedilo gumba"
                    ),
                ),
            ],
            options={
                "verbose_name": "Stran z besedilom",
                "verbose_name_plural": "Strani z besedilom",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.AlterModelOptions(
            name="homepage",
            options={
                "verbose_name": "Domača stran",
                "verbose_name_plural": "Domača stran",
            },
        ),
        migrations.AddField(
            model_name="homepage",
            name="button_text",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Besedilo gumba"
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="description",
            field=wagtail.fields.RichTextField(blank=True, verbose_name="Opis"),
        ),
        migrations.CreateModel(
            name="ChapterPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Opis")),
                (
                    "locked_by_default",
                    models.BooleanField(
                        default=False, verbose_name="Privzeto zaklenjeno"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Slika",
                    ),
                ),
            ],
            options={
                "verbose_name": "Poglavje",
                "verbose_name_plural": "Poglavja",
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="ChapterQuizSubPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "answers",
                    wagtail.fields.StreamField(
                        [("answer", 2)],
                        blank=True,
                        block_lookup={
                            0: ("wagtail.blocks.CharBlock", (), {"label": "Besedilo"}),
                            1: (
                                "wagtail.blocks.BooleanBlock",
                                (),
                                {"label": "Pravilno"},
                            ),
                            2: (
                                "wagtail.blocks.StructBlock",
                                [[("text", 0), ("correct", 1)]],
                                {"label": "Odgovor"},
                            ),
                        },
                        verbose_name="Odgovori",
                    ),
                ),
                ("points", models.IntegerField(default=0, verbose_name="Število točk")),
                (
                    "answer_description",
                    wagtail.fields.RichTextField(
                        blank=True, verbose_name="Opis odgovora"
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Slika",
                    ),
                ),
                (
                    "image_answer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Slika odgovora",
                    ),
                ),
            ],
            options={
                "verbose_name": "Stran s kvizom",
                "verbose_name_plural": "Strani s kvizom",
            },
            bases=("wagtailcore.page",),
        ),
    ]