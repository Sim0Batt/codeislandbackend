# Generated by Django 5.1.6 on 2025-03-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_project_description_es_project_short_description_es_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='short_descriptionEn',
            field=models.TextField(default='Default short in English'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_descriptionIt',
            field=models.TextField(default='Default short in Italian'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description_es',
            field=models.TextField(blank=True, null=True),
        ),
    ]
