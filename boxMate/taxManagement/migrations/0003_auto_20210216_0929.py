# Generated by Django 2.2.6 on 2021-02-16 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxManagement', '0002_auto_20210216_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceheader',
            name='date_time_issued',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 16, 9, 29, 36, 773573), null=True),
        ),
    ]
