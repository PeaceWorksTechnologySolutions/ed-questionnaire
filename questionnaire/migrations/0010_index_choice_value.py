# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_dbstylesheet_inclusion_tag'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='choice',
            index_together=set([('value',)]),
        ),
    ]
