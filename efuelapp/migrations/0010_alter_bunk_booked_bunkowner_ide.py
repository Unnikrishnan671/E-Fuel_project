# Generated by Django 3.2.12 on 2022-05-02 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0009_alter_bunk_booked_bunkowner_ide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bunk_booked',
            name='bunkowner_ide',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
