from django.core.management.base import BaseCommand

from faker import Faker

from studyProgram.models import Student


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker(['ru_RU'])
        fake_eng = Faker()
        for _ in range(100):
            Student.objects.create(
                name = fake_eng.first_name_nonbinary(),
                description = fake.name() 
            )
