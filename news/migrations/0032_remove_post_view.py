# Generated by Django 3.2.2 on 2021-06-18 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0031_post_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view',
        ),
    ]
