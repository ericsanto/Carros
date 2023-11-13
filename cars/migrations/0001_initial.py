# Generated by Django 4.2.7 on 2023-11-06 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.model')),
            ],
        ),
    ]