# Generated by Django 4.0.2 on 2022-02-18 12:23

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='discreption',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise control', 'Cruise control'), ('Audio interface', 'Audio interface'), ('Airbags', 'Airbags'), ('Air condition', 'Air condition'), ('seat heating', 'seat heating'), ('Alram system', 'Alram system'), ('parkassist', 'parkassist'), ('power steering', 'power steering'), ('revers camera', 'revers camera'), ('Direct fuel injection', 'Direct fuel injection'), ('Auto start/stop', 'Auto start/stop'), ('wind deflector', 'wind deflector'), ('Bluetooth handset', 'Bluetooth handset')], max_length=189),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]