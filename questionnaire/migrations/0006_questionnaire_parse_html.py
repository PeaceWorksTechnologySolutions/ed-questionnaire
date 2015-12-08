# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_questionset_parse_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='parse_html',
            field=models.BooleanField(default=False, verbose_name=b'parse questionnaire name as html?'),
        ),
    ]
