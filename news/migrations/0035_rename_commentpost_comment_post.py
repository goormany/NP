# Generated by Django 3.2.2 on 2021-07-11 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0034_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentPost',
            new_name='post',
        ),
    ]
