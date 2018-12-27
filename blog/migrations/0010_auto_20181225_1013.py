# Generated by Django 2.1.4 on 2018-12-25 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181225_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post2category', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post2contents', to='blog.Category'),
        ),
    ]