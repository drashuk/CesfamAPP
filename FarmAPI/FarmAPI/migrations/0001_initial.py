# Generated by Django 4.0.4 on 2022-04-19 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreMed', models.CharField(max_length=100)),
                ('miligramos', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('precio', models.CharField(max_length=20)),
                ('disponible', models.BooleanField()),
                ('no_disponible', models.BooleanField()),
                ('imagen', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
