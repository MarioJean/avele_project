# Generated by Django 3.1.2 on 2021-10-02 11:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='article',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
