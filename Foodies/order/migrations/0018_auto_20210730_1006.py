# Generated by Django 3.2.3 on 2021-07-30 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0017_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cart',
        ),
        migrations.AddField(
            model_name='orders',
            name='card_number',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='card_type',
            field=models.CharField(default='Card type', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='exp_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='order.orderitem'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Cart_details',
        ),
    ]
