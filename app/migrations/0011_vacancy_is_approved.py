# Generated by Django 4.2.4 on 2023-08-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
