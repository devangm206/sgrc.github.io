# Generated by Django 3.2.7 on 2021-11-09 17:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sgrc', '0002_remove_studentgriev_entered_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgriev',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentgriev',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]