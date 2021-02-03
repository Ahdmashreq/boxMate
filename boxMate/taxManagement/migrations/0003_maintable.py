# Generated by Django 2.2.6 on 2021-02-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxManagement', '0002_auto_20210203_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, max_length=20, null=True)),
                ('document_type_version', models.CharField(blank=True, max_length=20, null=True)),
                ('date_time_issued', models.DateTimeField()),
                ('taxpayer_activity_code', models.CharField(blank=True, max_length=20, null=True)),
                ('internal_id', models.CharField(blank=True, max_length=20, null=True)),
                ('purchase_order_reference', models.CharField(blank=True, max_length=55, null=True)),
                ('purchase_order_description', models.CharField(blank=True, max_length=55, null=True)),
                ('sales_order_reference', models.CharField(blank=True, max_length=20, null=True)),
                ('sales_order_description', models.CharField(blank=True, max_length=20, null=True)),
                ('proforma_invoice_number', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sales_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total_discount_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('net_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total_items_discount_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('extra_discount_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('issuer_type', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_registration_num', models.CharField(blank=True, max_length=20, null=True)),
                ('issuer_name', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_building_num', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_room', models.CharField(blank=True, max_length=20, null=True)),
                ('issuer_floor', models.CharField(blank=True, max_length=29, null=True)),
                ('issuer_street', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_land_mark', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_additional_information', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_governate', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_region_city', models.CharField(blank=True, max_length=55, null=True)),
                ('issuer_postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('issuer_country', models.CharField(blank=True, max_length=20, null=True)),
                ('issuer_branch_id', models.CharField(blank=True, max_length=20, null=True)),
                ('receiver_type', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_registration_num', models.CharField(blank=True, max_length=20, null=True)),
                ('receiver_name', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_building_num', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_room', models.CharField(blank=True, max_length=20, null=True)),
                ('receiver_floor', models.CharField(blank=True, max_length=5, null=True)),
                ('receiver_street', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_land_mark', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_additional_information', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_governate', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_region_city', models.CharField(blank=True, max_length=55, null=True)),
                ('receiver_postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('receiver_country', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_address', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_account_no', models.CharField(blank=True, max_length=55, null=True)),
                ('bank_account_iban', models.CharField(blank=True, max_length=55, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=20, null=True)),
                ('payment_terms', models.CharField(blank=True, max_length=20, null=True)),
                ('approach', models.CharField(blank=True, max_length=20, null=True)),
                ('packaging', models.CharField(blank=True, max_length=20, null=True)),
                ('date_validity', models.DateTimeField(blank=True, null=True)),
                ('export_port', models.CharField(blank=True, max_length=55, null=True)),
                ('country_of_origin', models.CharField(blank=True, max_length=55, null=True)),
                ('gross_weight', models.DecimalField(blank=True, decimal_places=6, max_digits=7, null=True)),
                ('net_weight', models.DecimalField(blank=True, decimal_places=6, max_digits=7, null=True)),
                ('delivery_terms', models.CharField(blank=True, max_length=55, null=True)),
                ('taxt_type', models.CharField(blank=True, max_length=55, null=True)),
                ('tax_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('signature_type', models.CharField(blank=True, max_length=55, null=True)),
                ('signature_value', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=55, null=True)),
                ('item_type', models.CharField(blank=True, max_length=20, null=True)),
                ('item_code', models.CharField(blank=True, max_length=55, null=True)),
                ('unit_type', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('sales_total', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('internal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('items_discount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('net_total', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total_taxable_fees', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('value_difference', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('currency_sold', models.CharField(blank=True, max_length=20, null=True)),
                ('amount_sold', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('amount_egp', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('currency_exchange_rate', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('discount_rate', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('taxt_item_type', models.CharField(blank=True, max_length=55, null=True)),
                ('tax_item_amount', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('tax_item_subtype', models.CharField(blank=True, max_length=55, null=True)),
                ('tax_item_rate', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
            ],
        ),
    ]
