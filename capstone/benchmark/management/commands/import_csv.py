import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from benchmark.models import Benchmark
from aimodels.models import AIModel
from device.models import Device

class Command(BaseCommand):
    help = 'Import CSV data into Benchmark model'

    def add_arguments(self, parser):
        # Argument to pass the CSV file path
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        try:
            with open(csv_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        # Get related objects by name
                        ai_model = AIModel.objects.get(name=row['ai_model'])
                        device = Device.objects.get(name=row['device'])

                        # Parse and clean data
                        runtime = row.get('runtime') or None
                        inference_time = float(row['inference_time'])

                        # Use only maximum memory usage
                        memory_usage = float(row['maximum_memory_usage']) if row.get('maximum_memory_usage') else None

                        compute_units = float(row['compute_units']) if row.get('compute_units') else None

                        # Parse test date
                        test_date = row.get('test_date') or datetime.today().date()
                        if isinstance(test_date, str):
                            test_date = datetime.strptime(test_date, "%Y-%m-%d").date()

                        notes = row.get('notes') or None

                        # Avoid duplicates using compound key
                        benchmark, created = Benchmark.objects.get_or_create(
                            ai_model=ai_model,
                            device=device,
                            test_date=test_date,
                            defaults={
                                'runtime': runtime,
                                'inference_time': inference_time,
                                'memory_usage': memory_usage,
                                'compute_units': compute_units,
                                'notes': notes,
                            }
                        )

                        if created:
                            self.stdout.write(self.style.SUCCESS(f"✅ Created Benchmark: {benchmark}"))
                        else:
                            self.stdout.write(self.style.WARNING(f"⚠️ Skipped duplicate Benchmark: {benchmark}"))

                    except AIModel.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"❌ AIModel not found: {row['ai_model']}"))
                    except Device.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f"❌ Device not found: {row['device']}"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"❌ Error processing row: {row}\n   {e}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ File not found: {csv_file}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error reading CSV file: {e}"))
