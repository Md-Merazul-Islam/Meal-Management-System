# Generated by Django 5.1.7 on 2025-05-17 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_freeboxrequest_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
