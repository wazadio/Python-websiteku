# Generated by Django 3.1.4 on 2021-01-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0004_auto_20210105_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='matakuliah',
            field=models.CharField(max_length=20),
        ),
    ]
