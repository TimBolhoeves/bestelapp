# Generated by Django 4.1 on 2022-08-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Broodjeshuis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('nummer', models.CharField(max_length=255)),
                ('datum', models.DateField(auto_now_add=True)),
                ('datumExact', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Walvis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('nummer', models.CharField(max_length=255)),
                ('datum', models.DateField(auto_now_add=True)),
                ('datumExact', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
