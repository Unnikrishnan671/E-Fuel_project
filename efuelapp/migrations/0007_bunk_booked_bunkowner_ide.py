# Generated by Django 3.2.12 on 2022-05-01 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0006_auto_20220428_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunk_booked',
            name='bunkowner_ide',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
