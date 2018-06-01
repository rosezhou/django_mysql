# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='board',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('bname', models.CharField(max_length=20)),
                ('bemail', models.CharField(max_length=500)),
                ('bsite', models.CharField(max_length=500)),
                ('bleave', models.TextField()),
            ],
        ),
    ]
