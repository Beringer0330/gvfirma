# Generated by Django 3.1.2 on 2021-11-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_asociados_tipoasociado'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientesAsesorados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='clientes')),
            ],
        ),
    ]
