# Generated by Django 2.2.6 on 2021-02-10 09:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuertax',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 2, 10, 9, 10, 10, 365580, tzinfo=utc), null=True),
        ),
    ]
