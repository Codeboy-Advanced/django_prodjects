# Generated by Django 5.1.5 on 2025-03-05 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin', '0002_cointype_remove_coin_desc_remove_coin_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='name',
            field=models.ForeignKey(default='bad coin name', on_delete=django.db.models.deletion.CASCADE, to='coin.cointype'),
        ),
        migrations.AlterField(
            model_name='cointype',
            name='desc',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='cointype',
            name='name',
            field=models.CharField(default='bad coin name', max_length=32),
        ),
    ]
