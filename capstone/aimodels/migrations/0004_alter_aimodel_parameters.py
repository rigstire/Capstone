# Generated by Django 5.2 on 2025-04-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aimodels', '0003_remove_aimodel_architecture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='parameters',
            field=models.CharField(blank=True, null=True),
        ),
    ]
