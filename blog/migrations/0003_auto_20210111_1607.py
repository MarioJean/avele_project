# Generated by Django 3.1.2 on 2021-01-11 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='Lifestyle', max_length=20),
        ),
    ]
