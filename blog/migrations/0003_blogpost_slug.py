# Generated by Django 2.2.1 on 2019-05-03 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default='hello-word'),
            preserve_default=False,
        ),
    ]
