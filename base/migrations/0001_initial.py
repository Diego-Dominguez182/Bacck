# Generated by Django 5.1.4 on 2024-12-08 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('champion_name', models.CharField(max_length=100)),
                ('item_1', models.CharField(max_length=100)),
                ('item_2', models.CharField(max_length=100)),
                ('item_3', models.CharField(max_length=100)),
                ('item_4', models.CharField(max_length=100)),
                ('item_5', models.CharField(max_length=100)),
                ('item_6', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'builds',
            },
        ),
    ]
