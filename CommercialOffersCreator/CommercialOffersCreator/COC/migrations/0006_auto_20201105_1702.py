# Generated by Django 3.1.2 on 2020-11-05 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('COC', '0005_auto_20201105_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricegroupdiscount',
            name='price_group',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='COC.pricegroup'),
        ),
    ]
