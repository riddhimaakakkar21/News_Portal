# Generated by Django 4.1.2 on 2023-01-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_submit',
            name='is_live',
            field=models.IntegerField(default=0),
        ),
    ]