# Generated by Django 3.2.3 on 2021-07-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_alter_orderitem_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='street',
            field=models.CharField(max_length=500, null=True),
        ),
    ]