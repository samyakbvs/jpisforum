# Generated by Django 2.1 on 2019-07-30 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_considered',
            field=models.BooleanField(default=False),
        ),
    ]