# Generated by Django 4.1.3 on 2022-11-13 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_unit_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inwarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('pur_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vendor')),
            ],
        ),
    ]
