# Generated by Django 4.1 on 2022-09-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_masks_vaccines_remove_profile_symptoms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptoms',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='app/static/'),
        ),
    ]
