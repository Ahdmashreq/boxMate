# Generated by Django 2.2.6 on 2021-02-10 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxManagement', '0003_auto_20210210_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceheader',
            name='date_time_issued',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 10, 9, 10, 18, 786716), null=True),
        ),
    ]
