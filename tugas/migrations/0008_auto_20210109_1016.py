# Generated by Django 3.1.4 on 2021-01-09 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0007_auto_20210106_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='matakuliah',
            field=models.CharField(max_length=50),
        ),
    ]