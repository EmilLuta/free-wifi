# Generated by Django 3.0.7 on 2020-06-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wifi', '0002_password_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
