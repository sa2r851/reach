# Generated by Django 4.1.7 on 2023-04-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_subsection_item_subsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='warning',
            field=models.TextField(default='لا يوجد تحذيرات', max_length=300),
        ),
    ]
