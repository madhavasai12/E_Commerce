# Generated by Django 5.0.1 on 2024-03-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contact_us_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
