# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_dbstylesheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbstylesheet',
            name='inclusion_tag',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
