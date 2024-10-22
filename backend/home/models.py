from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import BooleanBlock, CharBlock, StructBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page


class HomePage(Page):
    description = RichTextField(
        blank=True,
        verbose_name="Opis",
    )
    button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Besedilo gumba",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("button_text"),
    ]

    parent_page_types = []

    class Meta:
        verbose_name = "Domača stran"
        verbose_name_plural = "Domača stran"


class ChapterPage(Page):
    description = models.TextField(
        blank=True,
        verbose_name="Opis",
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika",
    )
    locked_by_default = models.BooleanField(
        default=False,
        verbose_name="Privzeto zaklenjeno",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("locked_by_default"),
    ]

    parent_page_types = ["home.HomePage"]

    class Meta:
        verbose_name = "Poglavje"
        verbose_name_plural = "Poglavja"


class ChapterTextSubPage(Page):
    text = RichTextField(
        blank=True,
        verbose_name="Besedilo",
    )
    button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Besedilo gumba",
    )

    content_panels = Page.content_panels + [
        FieldPanel("text"),
        FieldPanel("button_text"),
    ]

    parent_page_types = ["home.ChapterPage"]

    class Meta:
        verbose_name = "Stran z besedilom"
        verbose_name_plural = "Strani z besedilom"


class ChapterQuizSubPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika",
    )
    image_answer = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Slika odgovora",
    )
    answers = StreamField(
        [
            (
                "answer",
                StructBlock(
                    [
                        ("text", CharBlock(label="Besedilo")),
                        ("correct", BooleanBlock(required=False, label="Pravilno")),
                    ],
                    label="Odgovor",
                ),
            ),
        ],
        blank=True,
        use_json_field=True,
        verbose_name="Odgovori",
    )
    points = models.IntegerField(default=0, verbose_name="Število točk")
    answer_description = RichTextField(blank=True, verbose_name="Opis odgovora")

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("image_answer"),
        FieldPanel("answers"),
        FieldPanel("points"),
        FieldPanel("answer_description"),
    ]

    parent_page_types = ["home.ChapterPage"]

    class Meta:
        verbose_name = "Stran s kvizom"
        verbose_name_plural = "Strani s kvizom"
