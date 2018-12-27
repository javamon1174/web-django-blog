# Generated by Django 2.1.4 on 2018-12-25 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181225_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='media_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='content',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='content',
            name='text',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.Category'),
        ),
    ]