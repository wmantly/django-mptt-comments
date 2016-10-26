# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mptt_comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mpttcomment',
            name='accepted_answer',
            field=models.BooleanField(default=False),
        ),
    ]
