# Generated by Django 3.2.7 on 2021-09-26 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caucaSostenible', '0002_delete_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Undertaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=600)),
                ('location', models.CharField(max_length=40)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]