# Generated by Django 4.0.5 on 2022-08-04 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
