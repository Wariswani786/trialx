# Generated by Django 5.2.3 on 2025-07-23 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_patientprofile_delete_healthprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTrial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
    ]
