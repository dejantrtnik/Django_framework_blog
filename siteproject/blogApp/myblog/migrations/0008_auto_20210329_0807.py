# Generated by Django 3.1.7 on 2021-03-29 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_post_snnipet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='snnipet',
            new_name='snippet',
        ),
    ]
