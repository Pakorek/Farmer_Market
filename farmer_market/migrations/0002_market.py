# Generated by Django 2.0 on 2020-08-24 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=12)),
                ('_from', models.CharField(max_length=5)),
                ('_to', models.CharField(max_length=5)),
                ('long', models.SmallIntegerField()),
                ('lat', models.SmallIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmer_market.City')),
            ],
            options={
                'verbose_name': 'market',
                'ordering': ['city'],
            },
        ),
    ]
