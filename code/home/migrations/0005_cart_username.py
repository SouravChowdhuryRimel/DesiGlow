# Generated by Django 4.2.5 on 2023-09-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='username',
            field=models.CharField(blank=True, max_length=99, null=True),
        ),
    ]