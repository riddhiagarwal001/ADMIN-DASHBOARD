# Generated by Django 4.1.3 on 2022-11-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_inventory_issue_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='total_amount',
            field=models.FloatField(editable=False),
        ),
    ]
