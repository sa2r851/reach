# Generated by Django 4.1.7 on 2023-05-09 21:21

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='branch',
            field=models.CharField(choices=[('قلب', 'قلب')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='delivery_cost',
            field=models.FloatField(default=100.0),
        ),
        migrations.AddField(
            model_name='country',
            name='delivery_cost',
            field=models.FloatField(default=100.0),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('قلب', 'قلب')], max_length=20)),
                ('whats_app', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('whats_app2', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('staff', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pharmacy', to='account.pharmacy')),
            ],
        ),
    ]
