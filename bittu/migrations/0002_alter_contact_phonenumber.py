# Generated by Django 4.2.5 on 2023-12-06 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bittu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='PhoneNumber',
            field=models.IntegerField(),
        ),
    ]
