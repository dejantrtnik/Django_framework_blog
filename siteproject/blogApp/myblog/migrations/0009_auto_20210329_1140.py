# Generated by Django 3.1.7 on 2021-03-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0008_auto_20210329_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headers_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=255),
        ),
    ]
