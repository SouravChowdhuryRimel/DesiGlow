# Generated by Django 4.2.5 on 2023-11-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_wholesale_quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, choices=[('Health Care', 'Health Care'), ('Beauty Product', 'Beauty Product'), ('Organic', 'Organic'), ('Physiotherapy', 'Physiotherapy'), ('Hospital Eqquipment', 'Hospital Eqquipment'), ('Surgical Product', 'Surgical Product'), ('Lab Product', 'Lab Product'), ('Eye Product', 'Eye Product'), ('Dental Product', 'Dental Product'), ('Wholesale', 'Wholesale')], max_length=99, null=True),
        ),
    ]
