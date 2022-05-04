# Generated by Django 3.2.12 on 2022-05-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0012_alter_bunk_owner_ide'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ide', models.CharField(max_length=240, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('payment', models.CharField(max_length=240, null=True)),
                ('bank', models.CharField(max_length=240, null=True)),
                ('accountnumber', models.CharField(max_length=240, null=True)),
                ('ifse', models.CharField(max_length=240, null=True)),
            ],
        ),
    ]
