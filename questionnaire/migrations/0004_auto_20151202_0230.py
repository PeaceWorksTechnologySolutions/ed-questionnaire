# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20151129_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='parse_html',
            field=models.BooleanField(default=False, verbose_name=b'parse question text and footer as html?'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(help_text="Determines the means of answering the question. An open question gives the user a single-line textfield, multiple-choice gives the user a number of choices he/she can choose from. If a question is multiple-choice, enter the choices this user can choose from below'.", max_length=32, verbose_name='Type of question'),
        ),
    ]
