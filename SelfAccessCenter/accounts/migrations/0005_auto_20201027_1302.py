# Generated by Django 3.1.2 on 2020-10-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201027_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='abstrak',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
