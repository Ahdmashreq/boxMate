# Generated by Django 2.2.6 on 2021-02-07 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0002_auto_20210207_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuertax',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 7, 15, 4, 1, 140804, tzinfo=utc), null=True),
        ),
    ]