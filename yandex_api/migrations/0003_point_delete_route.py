# Generated by Django 5.0.3 on 2024-03-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_api', '0002_route_delete_distancetime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Route',
        ),
    ]
