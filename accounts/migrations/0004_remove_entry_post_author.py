# Generated by Django 3.0 on 2020-05-18 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_entry_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='post_author',
        ),
    ]
