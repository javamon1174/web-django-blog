# Generated by Django 2.1.4 on 2018-12-25 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181225_0958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contents',
            new_name='Content',
        ),
    ]