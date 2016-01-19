# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_questionset_questionnaire_and_sortid_index'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='answer',
            index_together=set([('subject', 'runid', 'id'), ('subject', 'runid')]),
        ),
    ]
