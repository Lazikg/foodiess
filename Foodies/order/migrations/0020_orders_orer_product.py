# Generated by Django 3.2.3 on 2021-07-30 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_auto_20210730_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orer_product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='order.orderproudcts'),
            preserve_default=False,
        ),
    ]
