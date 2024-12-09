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

    admin_default_ordering = "ord"

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
        verbose_name="Slika (če je SVG formata, bo barva #9BF37E zamenjana z drugo barvo glede na stanje)",
    )
    locked_by_default = models.BooleanField(
        default=False,
        verbose_name="Privzeto zaklenjeno",
    )
    is_feedback = models.BooleanField(
        default=False,
        verbose_name="Je anketa",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("image"),
        FieldPanel("locked_by_default"),
        FieldPanel("is_feedback"),
    ]

    parent_page_types = ["home.HomePage"]

    admin_default_ordering = "ord"

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

    admin_default_ordering = "ord"

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
    question = models.TextField(
        blank=True,
        verbose_name="Vprašanje",
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
    button_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Besedilo gumba",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("image_answer"),
        FieldPanel("question"),
        FieldPanel("answers"),
        FieldPanel("points"),
        FieldPanel("answer_description"),
        FieldPanel("button_text"),
    ]

    parent_page_types = ["home.ChapterPage"]

    admin_default_ordering = "ord"

    class Meta:
        verbose_name = "Stran s kvizom"
        verbose_name_plural = "Strani s kvizom"


class PageAnswerData(models.Model):
    page = models.ForeignKey(
        "home.ChapterQuizSubPage",
        on_delete=models.CASCADE,
        verbose_name="Stran",
    )
    answer_index = models.IntegerField(verbose_name="Indeks odgovora")
    correct = models.BooleanField(verbose_name="Pravilno")

    def __str__(self):
        return f"{self.page.title} - {self.answer_index} - {self.correct}"

    class Meta:
        verbose_name = "Odgovor na stran"
        verbose_name_plural = "Odgovori na stran"


class FinishedChapterData(models.Model):
    finished_at = models.DateTimeField(auto_now_add=True, verbose_name="Končano ob")
    user_guid = models.CharField(max_length=255, verbose_name="Uporabnik")
    chapter = models.ForeignKey(
        "home.ChapterPage",
        on_delete=models.CASCADE,
        verbose_name="Poglavje",
    )
    score = models.IntegerField(verbose_name="Število točk")
    answers = models.ManyToManyField("home.PageAnswerData", verbose_name="Odgovori")

    def __str__(self):
        return f"{self.user_guid} - {self.chapter.title}"

    class Meta:
        verbose_name = "Končano poglavje"
        verbose_name_plural = "Končana poglavja"
