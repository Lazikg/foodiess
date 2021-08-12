# Generated by Django 3.2.3 on 2021-07-30 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0002_product'),
        ('order', '0020_orders_orer_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproudcts',
            name='products',
        ),
        migrations.AddField(
            model_name='orderproudcts',
            name='products',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='Foods.product'),
            preserve_default=False,
        ),
    ]