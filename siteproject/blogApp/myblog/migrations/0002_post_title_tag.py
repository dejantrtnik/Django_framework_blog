# Generated by Django 3.1.7 on 2021-03-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Webproject', max_length=255),
        ),
    ]
