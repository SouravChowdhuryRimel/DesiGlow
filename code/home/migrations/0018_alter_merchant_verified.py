# Generated by Django 4.2.5 on 2023-09-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_merchant_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]