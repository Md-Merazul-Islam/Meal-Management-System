# Generated by Django 5.2 on 2025-06-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weekly_order_manage', '0002_stripecustomer_stripe_subscription_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
