# Generated by Django 4.2.2 on 2023-06-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
