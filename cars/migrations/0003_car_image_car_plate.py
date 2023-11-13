# Generated by Django 4.2.2 on 2023-11-06 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image',
            field=models.ImageField(default=1, upload_to='cars/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='plate',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]