# Generated by Django 4.1 on 2022-09-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_masks_image_alter_symptoms_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masks',
            name='protection',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
