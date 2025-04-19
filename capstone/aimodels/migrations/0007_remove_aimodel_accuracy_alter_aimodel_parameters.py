# Generated by Django 5.2 on 2025-04-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aimodels', '0006_alter_aimodel_parameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aimodel',
            name='accuracy',
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='parameters',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
