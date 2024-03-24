# Generated by Django 5.0.3 on 2024-03-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex_api', '0003_point_delete_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_point', models.CharField(max_length=100)),
                ('end_point', models.CharField(max_length=100)),
                ('distance', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Point',
        ),
    ]