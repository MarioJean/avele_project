# Generated by Django 3.1.2 on 2021-02-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210209_0205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog',
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]