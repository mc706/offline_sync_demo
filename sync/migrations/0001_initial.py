# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hash', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': b'hash',
                'verbose_name_plural': b'hashes',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='hash',
            unique_together=set([(b'account', b'hash')]),
        ),
    ]
