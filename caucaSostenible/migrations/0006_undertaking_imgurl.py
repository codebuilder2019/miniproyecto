# Generated by Django 3.2.7 on 2021-09-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caucaSostenible', '0005_investor'),
    ]

    operations = [
        migrations.AddField(
            model_name='undertaking',
            name='imgURL',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
