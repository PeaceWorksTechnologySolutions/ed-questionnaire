# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0016_subject_given_sur_name_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalStyles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='admin_access_only',
            field=models.BooleanField(default=False, verbose_name=b'Only allow access to logged in users? (This allows entering paper surveys without allowing new external submissions)'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='language',
            field=models.CharField(default=b'en-us', max_length=2, verbose_name='Language', choices=[(b'en', b'English')]),
        ),
    ]
