# Generated by Django 5.0.2 on 2024-02-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'wanafunzi',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
