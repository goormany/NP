# Generated by Django 3.2.2 on 2021-05-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20210521_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentText',
            field=models.TextField(max_length=60),
        ),
    ]
