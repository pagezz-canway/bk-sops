# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-05-22 07:07
from __future__ import unicode_literals

from django.db import migrations


def reserve_id_for_project(apps, schema_editor):
    min_id = 10000
    Project = apps.get_model('core', 'Project')
    Project.objects.create(
        id=min_id,
        name='DUMMY',
        time_zone='Asia/Shanghai',
        creator='DUMMY',
        desc=''
    )
    Project.objects.get(id=min_id).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0009_project_userdefaultproject'),
    ]

    operations = [
        migrations.RunPython(reserve_id_for_project)
    ]
