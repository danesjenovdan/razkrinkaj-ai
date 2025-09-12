from calendar import monthrange

from django.core.management.base import BaseCommand

from home.models import ChapterPage, HomePage


class Command(BaseCommand):
    help = "Generate a chapter page for every day in the provided year and month"

    def add_arguments(self, parser):
        parser.add_argument("year", type=int)
        parser.add_argument("month", type=int)

    def handle(self, *args, **options):
        year = options["year"]
        month = options["month"]
        num_days = monthrange(year, month)[1]

        # Delete all existing chapter pages
        self.stdout.write("Deleting existing chapter pages...")
        ChapterPage.objects.all().delete()

        home_page = HomePage.objects.first()

        # Generate a chapter page for each day of the month
        for date in range(1, num_days + 1):
            self.stdout.write(f"Generating page for {year}-{month:02}-{date:02}")
            home_page.add_child(instance=ChapterPage(title=f"{date}. {month}. {year}"))

        self.stdout.write(self.style.SUCCESS("Successfully generated chapter pages"))
