# Generated by Django 4.2.4 on 2023-08-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_vacancy_delete_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='email',
            field=models.CharField(default='am@gmail.com', max_length=200),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='telephone',
            field=models.IntegerField(default=712),
        ),
    ]
