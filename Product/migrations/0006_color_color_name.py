# Generated by Django 5.0.7 on 2024-08-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0005_remove_productvariation_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]