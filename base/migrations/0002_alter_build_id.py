# Generated by Django 5.1.4 on 2024-12-08 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
