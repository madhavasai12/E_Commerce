# Generated by Django 5.0.1 on 2024-03-09 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_product_price_morrisons_product_price_sainsburys_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_morrisons',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_sainsburys',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price_tesco',
        ),
    ]
