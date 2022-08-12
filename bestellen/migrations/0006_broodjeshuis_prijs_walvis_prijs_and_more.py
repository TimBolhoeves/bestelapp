# Generated by Django 4.1 on 2022-08-12 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellen', '0005_rename_keuzes_broodjeshuis_keuze_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='broodjeshuis',
            name='prijs',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
        migrations.AddField(
            model_name='walvis',
            name='prijs',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
        migrations.AlterField(
            model_name='broodjeshuis',
            name='keuze',
            field=models.TextField(default='Niet ingevuld'),
        ),
        migrations.AlterField(
            model_name='broodjeshuis',
            name='naam',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
        migrations.AlterField(
            model_name='broodjeshuis',
            name='nummer',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
        migrations.AlterField(
            model_name='walvis',
            name='keuze',
            field=models.TextField(default='Niet ingevuld'),
        ),
        migrations.AlterField(
            model_name='walvis',
            name='naam',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
        migrations.AlterField(
            model_name='walvis',
            name='nummer',
            field=models.CharField(default='Niet ingevuld', max_length=255),
        ),
    ]