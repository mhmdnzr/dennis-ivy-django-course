# Generated by Django 2.2.17 on 2022-08-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_alts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='alts',
            field=models.SlugField(),
        ),
    ]
