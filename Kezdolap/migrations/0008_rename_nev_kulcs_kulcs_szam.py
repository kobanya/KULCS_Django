# Generated by Django 4.2.6 on 2023-10-16 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kezdolap', '0007_rename_kulcs_szam_kulcs_nev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kulcs',
            old_name='nev',
            new_name='kulcs_szam',
        ),
    ]
