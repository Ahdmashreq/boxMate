# Generated by Django 2.2.6 on 2021-02-03 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taxManagement', '0005_auto_20210203_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintable',
            name='signature_value',
        ),
    ]
