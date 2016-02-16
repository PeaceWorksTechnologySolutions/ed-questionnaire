# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0017_auto_20160209_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='runinfohistory',
            name='completed',
            field=models.DateTimeField(),
        ),
    ]
