# Generated by Django 4.1.3 on 2022-11-13 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_sale_date_distribution_issued_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recieved_quantity', models.FloatField(default=0)),
                ('issued_quantity', models.FloatField(default=0)),
                ('total_balance_qty', models.FloatField()),
                ('issue', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.distribution')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('recieving', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.inwarding')),
            ],
            options={
                'verbose_name_plural': 'Inventory',
            },
        ),
    ]
