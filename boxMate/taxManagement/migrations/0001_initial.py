# Generated by Django 2.2.6 on 2021-02-24 05:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('codes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issuer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, choices=[('I', 'I')], default='I', max_length=2, null=True)),
                ('document_type_version', models.CharField(blank=True, choices=[('1.0', '1.0'), ('0.9', '0.9')], default='1.0', max_length=8, null=True)),
                ('date_time_issued', models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 24, 7, 57, 34, 503869), null=True)),
                ('internal_id', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_order_reference', models.CharField(blank=True, max_length=50, null=True)),
                ('purchase_order_description', models.CharField(blank=True, max_length=100, null=True)),
                ('sales_order_reference', models.CharField(blank=True, max_length=50, null=True)),
                ('sales_order_description', models.CharField(blank=True, max_length=100, null=True)),
                ('proforma_invoice_number', models.CharField(blank=True, max_length=50, null=True)),
                ('total_sales_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('total_discount_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('net_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('extra_discount_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('total_items_discount_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, max_digits=20, null=True)),
                ('issuer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issuer.Issuer')),
                ('issuer_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issuer_address', to='issuer.Address')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='issuer.Receiver')),
                ('receiver_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_address', to='issuer.Address')),
                ('taxpayer_activity_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codes.ActivityType')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('itemType', models.CharField(blank=True, help_text='Must be of GPC format', max_length=50, null=True)),
                ('itemCode', models.CharField(blank=True, help_text='Must be of GS1 code', max_length=50, null=True)),
                ('unitType', models.CharField(blank=True, help_text='A code from unitype table', max_length=50, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('currencySold', models.CharField(blank=True, help_text='Currency code used from ISO 4217.', max_length=10, null=True)),
                ('amountEGP', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('amountSold', models.DecimalField(blank=True, decimal_places=5, help_text='Mandatory if currencySold <> EGP.', max_digits=20, null=True)),
                ('currencyExchangeRate', models.DecimalField(blank=True, decimal_places=5, help_text='Exchange rate of the Egyptian bank on the day of invoicing used to convert currency sold to the value of currency EGP. Mandatory if currencySold is not EGP. Should be valid decimal with max 5 decimal digits.', max_digits=20, null=True)),
                ('salesTotal', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Total amount for the invoice line considering quantity and unit price in EGP (with excluded factory amounts if they are present for specific types in documents).', max_digits=20, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Total amount for the invoice line after adding all pricing items, taxes, removing discounts.', max_digits=20, null=True)),
                ('valueDifference', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Value difference when selling goods already taxed (accepts +/- numbers), e.g., factory value based.', max_digits=20, null=True)),
                ('totalTaxableFees', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Total amount of additional taxable fees to be used in final tax calculation.', max_digits=20, null=True)),
                ('itemsDiscount', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Non-taxable items discount.', max_digits=20, null=True)),
                ('netTotal', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Total amount for the invoice line after applying discount.', max_digits=20, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=1, help_text='Optional: discount percentage rate applied. Must be from 0 to 100.', max_digits=5, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=5, default=0.0, help_text='Optional: amount of discount provided to customer for this item. Should be smaller or equal to value Total. If percentage specified should be valid amount calculated from total by applying discount percentage. ', max_digits=20, null=True)),
                ('internalCode', models.CharField(blank=True, help_text='Optional: Internal code used for the product being sold – can be used to simplify references back to existing solution.', max_length=50, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='line_created_by', to=settings.AUTH_USER_MODEL)),
                ('invoice_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='taxManagement.InvoiceHeader')),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(blank=True, max_length=20, null=True)),
                ('document_type_version', models.CharField(blank=True, max_length=20, null=True)),
                ('date_time_issued', models.DateTimeField(blank=True, null=True)),
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
                ('gross_weight', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('net_weight', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
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
                ('value_difference', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=10, max_digits=20, null=True)),
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
        migrations.CreateModel(
            name='TaxLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('last_updated_at', models.DateField(auto_now=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tax_line_created_by', to=settings.AUTH_USER_MODEL)),
                ('invoice_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tax_lines', to='taxManagement.InvoiceLine')),
                ('last_updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codes.TaxSubtypes')),
                ('taxType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codes.TaxTypes')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subm_id', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('subm_uuid', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('document_count', models.IntegerField(blank=True, null=True)),
                ('date_time_received', models.DateTimeField(blank=True, null=True)),
                ('over_all_status', models.CharField(blank=True, max_length=100, null=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxManagement.InvoiceHeader')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_type', models.CharField(blank=True, max_length=20, null=True)),
                ('signature_value', models.TextField(blank=True, null=True)),
                ('invoice_header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signatures', to='taxManagement.InvoiceHeader')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderTaxTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=5, max_digits=20, null=True)),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taxManagement.InvoiceHeader')),
                ('tax', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='codes.TaxTypes')),
            ],
        ),
    ]
