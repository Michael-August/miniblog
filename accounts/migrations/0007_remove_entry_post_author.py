# Generated by Django 3.0 on 2020-05-19 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200518_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='post_author',
        ),
    ]
