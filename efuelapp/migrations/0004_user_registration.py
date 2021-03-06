# Generated by Django 3.2.12 on 2022-04-28 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efuelapp', '0003_auto_20220427_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240, null=True)),
            ],
        ),
    ]
