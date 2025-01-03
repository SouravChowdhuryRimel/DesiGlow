# Generated by Django 4.2.5 on 2023-09-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_product_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='verified',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='additional_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
