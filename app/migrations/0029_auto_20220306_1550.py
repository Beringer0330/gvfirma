# Generated by Django 3.1.2 on 2022-03-06 20:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20220226_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonios',
            name='descripcion',
            field=ckeditor.fields.RichTextField(max_length=600, verbose_name='Descripcion'),
        ),
    ]
