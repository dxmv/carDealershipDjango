# Generated by Django 3.2.4 on 2021-08-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='likes_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
