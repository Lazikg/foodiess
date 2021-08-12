# Generated by Django 3.2.5 on 2021-07-28 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Foods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('desc', models.TextField(max_length=100, null=True)),
                ('image', models.ImageField(upload_to='media/menu_images/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Foods.category')),
            ],
        ),
    ]