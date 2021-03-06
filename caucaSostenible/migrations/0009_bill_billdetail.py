# Generated by Django 3.2.7 on 2021-09-26 17:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caucaSostenible', '0008_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caucaSostenible.bill')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caucaSostenible.product')),
            ],
        ),
    ]
