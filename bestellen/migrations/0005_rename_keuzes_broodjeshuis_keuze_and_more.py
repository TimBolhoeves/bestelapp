# Generated by Django 4.1 on 2022-08-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bestellen', '0004_rename_keuze_broodjeshuis_keuzes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='broodjeshuis',
            old_name='keuzes',
            new_name='keuze',
        ),
        migrations.RenameField(
            model_name='walvis',
            old_name='keuzes',
            new_name='keuze',
        ),
    ]
