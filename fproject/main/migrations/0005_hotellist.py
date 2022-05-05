# Generated by Django 4.0.2 on 2022-03-24 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelName', models.CharField(max_length=100, verbose_name='Name of hotel')),
                ('cityName', models.CharField(max_length=80, verbose_name='City name')),
                ('hotel_img', models.ImageField(upload_to='hotelMedia/')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
            },
        ),
    ]
