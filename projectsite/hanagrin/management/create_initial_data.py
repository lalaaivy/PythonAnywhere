from django.core.management.base import BaseCommand
from faker import Faker
from hanagrin.models import Task, Note, SubTask, Category, Priority
from django.utils import timezone

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_tasks(10)
        self.create_notes(10)
        self.create_subtasks(10)

    def create_tasks(self, count):
        fake = Faker()

        for _ in range(count):

            Task.objects.create(
                task_title=fake.sentence(nb_words=5),
                task_description=fake.paragraph(nb_sentences=3),
                task_deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=("Pending", "In Progress", "Completed")),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first(),
            )


    def create_notes(self, count):
        fake = Faker()

        for _ in range(count):
            Note.objects.create(
                note_content=fake.paragraph(nb_sentences=3)
            )

    def create_subtasks(self, count):
        fake = Faker()

        for _ in range(count):
            SubTask.objects.create(
                subTask_title=fake.sentence(nb_words=5),
                subTask_description=fake.paragraph(nb_sentences=3),
                parent_task=Task.objects.order_by('?').first()
            )
    