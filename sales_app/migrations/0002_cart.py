# Generated by Django 5.0.4 on 2024-05-09 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_status5', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_cart', to='sales_app.mobile_rentals')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_cart', to='sales_app.customer')),
            ],
        ),
    ]
