# Generated by Django 5.2.3 on 2025-07-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_clinicaltrial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicaltrial',
            name='exclusion_criteria',
            field=models.TextField(default='Not specified'),
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='inclusion_criteria',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinicaltrial',
            name='location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
