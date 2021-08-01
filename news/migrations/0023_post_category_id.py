# Generated by Django 3.2.2 on 2021-06-16 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0022_alter_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_id', to='news.category', verbose_name='Категория'),
        ),
    ]
