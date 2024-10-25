# Generated by Django 5.1.2 on 2024-10-24 21:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order_deliveryproof'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Address', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='City', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='Country', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='First', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(default='Last', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='order_notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='0000000000', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='postcode',
            field=models.CharField(default='000000', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='State', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
