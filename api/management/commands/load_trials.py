from django.core.management.base import BaseCommand
import json
from api.models import ClinicalTrial

class Command(BaseCommand):
    help = 'Load clinical trials from dummy_trials.json'

    def handle(self, *args, **kwargs):
        with open('dummy_trials.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            created = 0
            for item in data:
                ClinicalTrial.objects.create(
                    title=item["title"],
                    inclusion_criteria=item["inclusion_criteria"],
                    exclusion_criteria=item["exclusion_criteria"],
                    location=item["location"]
                )
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {created} clinical trials.'))
