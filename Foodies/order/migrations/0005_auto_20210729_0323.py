# Generated by Django 3.2.3 on 2021-07-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0002_product'),
        ('order', '0004_remove_orders_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='phone',
            field=models.CharField(max_length=13, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='orders',
            name='products',
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ManyToManyField(blank=True, to='Foods.Product'),
        ),
    ]
