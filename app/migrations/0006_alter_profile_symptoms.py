# Generated by Django 4.1 on 2022-09-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_profile_symptoms_profile_symptoms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='symptoms',
            field=models.ManyToManyField(blank=True, to='app.symptoms'),
        ),
    ]
