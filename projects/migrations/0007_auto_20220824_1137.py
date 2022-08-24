# Generated by Django 2.2.17 on 2022-08-24 07:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20220824_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='alts',
        ),
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
