# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-19 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0019_og_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_script',
            field=models.TextField(default=b'', help_text=b'User-defined JavaScript for site customization.', max_length=65536, verbose_name=b'User script'),
        ),
    ]