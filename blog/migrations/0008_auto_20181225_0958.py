# Generated by Django 2.1.4 on 2018-12-25 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20181225_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(max_length=50)),
                ('text', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField(blank=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='created_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post2category', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post2contents', to='blog.Category'),
        ),
    ]
