# Generated by Django 4.2.7 on 2023-11-11 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventory_alter_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
