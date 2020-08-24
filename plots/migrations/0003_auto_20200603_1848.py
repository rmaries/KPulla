# Generated by Django 3.0.5 on 2020-06-03 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0002_auto_20200530_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funds_db',
            name='FundName',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='AMFICode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plots.Funds_DB'),
        ),
    ]
