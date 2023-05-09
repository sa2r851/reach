# Generated by Django 4.1.7 on 2023-05-07 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('store', '0006_remove_cartoffers_cart_remove_cartoffers_offer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='branch',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='account.pharmacy'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='Pharmacy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_pharmacy', to='account.pharmacy'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='Pharmacy',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='account.pharmacy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_customer', to='account.customer'),
        ),
    ]
