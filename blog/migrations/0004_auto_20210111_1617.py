# Generated by Django 3.1.2 on 2021-01-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210111_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('green', 'green'), ('red', 'red')], max_length=20),
        ),
    ]
