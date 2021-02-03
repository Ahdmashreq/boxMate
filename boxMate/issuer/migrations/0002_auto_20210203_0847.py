# Generated by Django 2.2.6 on 2021-02-03 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issuer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='issuer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issuer.Issuer'),
        ),
        migrations.CreateModel(
            name='Reciever',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('B', 'business'), ('P', 'natural person'), ('F', 'foreigner')], default='B', max_length=8)),
                ('reg_num', models.CharField(max_length=8, verbose_name='reg_number')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='reciever name')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reciever_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issuer.Reciever'),
        ),
    ]
