# Generated by Django 3.1.2 on 2020-10-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201027_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='abstrak',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
