# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBlog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tittle', models.CharField(max_length=50, default='')),
                ('tittle_sm', models.CharField(max_length=50, default='')),
                ('body', django_markdown.models.MarkdownField(default='')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('publisher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('question_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='myblog',
            name='tag',
            field=models.ForeignKey(to='blog.Tag'),
        ),
    ]
