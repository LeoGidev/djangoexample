# Generated by Django 5.1.3 on 2024-11-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dato',
            fields=[
                ('Fecha', models.DateField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Dato', models.CharField(max_length=255)),
            ],
        ),
    ]
