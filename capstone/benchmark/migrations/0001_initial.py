# Generated by Django 4.2.19 on 2025-03-18 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aimodels', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateField(auto_now_add=True)),
                ('inference_time', models.FloatField(help_text='Time in milliseconds')),
                ('accuracy', models.FloatField(help_text='Accuracy as a percentage')),
                ('power_consumption', models.FloatField(blank=True, help_text='Power used in watts', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('ai_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benchmarks', to='aimodels.aimodel')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benchmarks', to='device.device')),
            ],
            options={
                'unique_together': {('ai_model', 'device', 'test_date')},
            },
        ),
    ]
