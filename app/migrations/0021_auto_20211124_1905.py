# Generated by Django 3.1.2 on 2021-11-25 00:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_service_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='intro_nosotros',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
