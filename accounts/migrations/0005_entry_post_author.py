# Generated by Django 3.0 on 2020-05-18 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_entry_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='post_author',
            field=models.CharField(default='cynarams', max_length=25),
        ),
    ]