# Generated by Django 3.1.2 on 2021-11-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_blog_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
    ]