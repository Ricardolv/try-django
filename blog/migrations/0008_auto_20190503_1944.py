# Generated by Django 2.2.1 on 2019-05-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190503_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', 'timestamp']},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='update',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
