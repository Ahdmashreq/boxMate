# Generated by Django 2.2.6 on 2021-03-10 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxManagement', '0004_auto_20210308_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceheader',
            name='date_time_issued',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 10, 13, 18, 33, 481287), null=True),
        ),
    ]