# Generated by Django 2.1 on 2019-07-24 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_anonymous'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvoted_users',
            field=models.TextField(default=''),
        ),
    ]
