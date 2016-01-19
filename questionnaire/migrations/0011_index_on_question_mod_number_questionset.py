# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_index_choice_value'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='question',
            index_together=set([('number', 'questionset')]),
        ),
    ]
