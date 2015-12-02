# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20151202_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionset',
            name='parse_html',
            field=models.BooleanField(default=False, verbose_name=b'parse questionset heading and text as html?'),
        ),
    ]
