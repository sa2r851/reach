# Generated by Django 4.1.7 on 2023-04-21 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='subsection',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.subsection'),
            preserve_default=False,
        ),
    ]
