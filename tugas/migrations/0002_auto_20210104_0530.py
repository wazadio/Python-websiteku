# Generated by Django 3.1.4 on 2021-01-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tugas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tugas',
            name='matakuliah',
            field=models.CharField(choices=[('hafis', 'hafis'), ('hafiz', 'hafiz')], max_length=20),
        ),
    ]
