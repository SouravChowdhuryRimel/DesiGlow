# Generated by Django 4.2.5 on 2023-10-03 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_rename_photo_product_photos_productimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
