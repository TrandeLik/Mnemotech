# Generated by Django 2.1 on 2018-08-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180820_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodule',
            name='ok',
            field=models.CharField(default='noAnswer', max_length=250),
        ),
    ]
