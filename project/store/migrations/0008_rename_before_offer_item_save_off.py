# Generated by Django 4.1.7 on 2023-05-08 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_doctor_branch_order_pharmacy_orderitems_pharmacy_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='before_offer',
            new_name='save_off',
        ),
    ]
