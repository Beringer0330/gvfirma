# Generated by Django 3.1.2 on 2022-03-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_service_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('numero', models.IntegerField()),
                ('asunto', models.TextField(max_length=600)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
