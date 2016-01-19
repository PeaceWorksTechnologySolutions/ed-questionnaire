# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0011_index_on_question_mod_number_questionset'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='questionset',
            index_together=set([('questionnaire', 'sortid')]),
        ),
    ]
