# Generated by Django 3.0.6 on 2020-05-27 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200527_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='My default Location', max_length=120, null=True),
        ),
    ]
