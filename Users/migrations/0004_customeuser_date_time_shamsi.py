# Generated by Django 5.0.7 on 2024-08-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customeuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='date_time_shamsi',
            field=models.DateTimeField(null=True),
        ),
    ]
