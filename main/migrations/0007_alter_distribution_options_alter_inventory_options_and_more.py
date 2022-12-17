# Generated by Django 4.1.3 on 2022-11-16 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_inventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distribution',
            options={'verbose_name_plural': '5.Distribution'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': '6.Inventory'},
        ),
        migrations.AlterModelOptions(
            name='inwarding',
            options={'verbose_name_plural': '4. Inwardings'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '3.Products'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': '2.Units'},
        ),
        migrations.AlterModelOptions(
            name='vendor',
            options={'verbose_name_plural': '1.Vendors'},
        ),
        migrations.AlterField(
            model_name='inventory',
            name='issue',
            field=models.ForeignKey(default=0, null=0, on_delete=django.db.models.deletion.CASCADE, to='main.distribution'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='issued_quantity',
            field=models.FloatField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='recieved_quantity',
            field=models.FloatField(default=0, null=0),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='recieving',
            field=models.ForeignKey(default=0, null=0, on_delete=django.db.models.deletion.CASCADE, to='main.inwarding'),
        ),
        migrations.AlterField(
            model_name='inwarding',
            name='total_amount',
            field=models.FloatField(default=0, editable=False),
        ),
    ]