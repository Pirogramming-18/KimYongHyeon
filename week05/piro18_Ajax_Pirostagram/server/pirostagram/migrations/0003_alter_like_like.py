# Generated by Django 4.1.5 on 2023-01-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirostagram', '0002_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]
