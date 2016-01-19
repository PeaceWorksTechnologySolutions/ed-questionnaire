# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0014__runinfo_index_random'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='questionset',
            index_together=set([('questionnaire', 'sortid'), ('sortid',)]),
        ),
    ]
