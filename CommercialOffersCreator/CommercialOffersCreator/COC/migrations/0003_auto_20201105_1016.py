# Generated by Django 3.1.2 on 2020-11-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('COC', '0002_auto_20201104_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
