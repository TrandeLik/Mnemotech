# Generated by Django 2.1 on 2018-08-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20180819_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mg',
            field=models.CharField(default='noMessage', max_length=200),
        ),
    ]
