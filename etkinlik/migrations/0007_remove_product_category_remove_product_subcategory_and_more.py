# Generated by Django 4.2.4 on 2023-08-19 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('etkinlik', '0006_category_product_subcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
