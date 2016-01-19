# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0013__answer_index_subject_run_id'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='runinfo',
            index_together=set([('random',)]),
        ),
    ]
