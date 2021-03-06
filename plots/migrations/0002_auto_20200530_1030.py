# Generated by Django 3.0.5 on 2020-05-30 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funds_db',
            name='id',
        ),
        migrations.AlterField(
            model_name='funds_db',
            name='SchemeCode',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Amount_Invested', models.DecimalField(decimal_places=2, max_digits=15)),
                ('AMFICode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plots.Funds_DB')),
            ],
        ),
    ]
