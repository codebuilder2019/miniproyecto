# Generated by Django 3.2.7 on 2021-09-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caucaSostenible', '0009_bill_billdetail'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='billdetail',
            unique_together={('bill', 'product')},
        ),
    ]