# Generated by Django 2.2.6 on 2019-12-25 15:55

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testruns', '0007_test_execution_statuses'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testexecutionstatus',
            options={'verbose_name_plural': 'Test execution statuses'},
        ),
        migrations.AlterField(
            model_name='testexecutionstatus',
            name='color',
            field=colorfield.fields.ColorField(max_length=18),
        ),
    ]