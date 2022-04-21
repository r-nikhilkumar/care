# Generated by Django 2.2.11 on 2022-04-21 17:33

import care.facility.models.asset
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0286_auto_20220316_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='qr_code_id',
            field=models.CharField(blank=True, default=care.facility.models.asset.get_random_asset_id, max_length=1024, unique=True),
        ),
    ]
