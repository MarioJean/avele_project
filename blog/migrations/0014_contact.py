# Generated by Django 3.1.2 on 2021-04-03 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210403_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('inquiry', models.TextField()),
                ('publish', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
