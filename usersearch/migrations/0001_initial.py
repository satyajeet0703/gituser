# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=200)),
                ('git_id', models.IntegerField()),
                ('avatar_url', models.URLField()),
                ('gravatar_id', models.CharField(blank=True, max_length=100)),
                ('url', models.URLField()),
                ('html_url', models.URLField()),
                ('followers_url', models.URLField()),
                ('following_url', models.URLField()),
                ('gists_url', models.URLField()),
                ('starred_url', models.URLField()),
                ('subscriptions_url', models.URLField()),
                ('organizations_url', models.URLField()),
                ('repos_url', models.URLField()),
                ('events_url', models.URLField()),
                ('received_events_url', models.URLField()),
                ('type', models.CharField(blank=True, default='User', max_length=200)),
                ('site_admin', models.BooleanField(default=False)),
                ('repos', models.IntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('language', models.CharField(blank=True, max_length=200)),
                ('followers', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('score', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
