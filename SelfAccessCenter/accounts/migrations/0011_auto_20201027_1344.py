# Generated by Django 3.1.2 on 2020-10-27 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201027_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='penulis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='document_penulis', to='accounts.account'),
        ),
    ]