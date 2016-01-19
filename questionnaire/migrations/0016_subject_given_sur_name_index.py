# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0015_questionnaire_index_sortid'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='subject',
            index_together=set([('givenname', 'surname')]),
        ),
    ]
