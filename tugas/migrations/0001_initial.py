# Generated by Django 3.1.4 on 2021-01-03 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tugas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matakuliah', models.CharField(choices=[('hafis', 'apis'), ('hafiz', 'apiz')], max_length=20)),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
