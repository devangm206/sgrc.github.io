# Generated by Django 3.2.7 on 2021-11-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgrc', '0003_auto_20211109_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgriev',
            name='is_solved',
            field=models.BooleanField(null=True),
        ),
    ]
