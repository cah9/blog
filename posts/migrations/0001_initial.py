# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Зоголовок поста')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('published', models.BooleanField(verbose_name='Опубликовано', default=False)),
            ],
        ),
    ]
