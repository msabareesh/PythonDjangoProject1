# Generated by Django 3.0.6 on 2020-05-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
