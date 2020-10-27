# Generated by Django 3.1.2 on 2020-10-27 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20201027_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='prodi',
            field=models.CharField(choices=[('Pendidikan', 'Pendidikan'), ('Sastra', 'Sastra')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='penulis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account'),
        ),
    ]
