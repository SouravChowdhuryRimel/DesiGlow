# Generated by Django 4.2.5 on 2023-10-03 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_myorder_payment_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='photo',
            new_name='photos',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_photo/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='home.product')),
            ],
        ),
    ]