# Generated by Django 2.2.5 on 2019-09-05 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibMysql', '0009_auto_20190905_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookclassify',
            old_name='typeid',
            new_name='classifyid',
        ),
        migrations.RenameField(
            model_name='bookstate',
            old_name='typeid',
            new_name='stateid',
        ),
        migrations.RenameField(
            model_name='havebookstate',
            old_name='typeid',
            new_name='stateid',
        ),
        migrations.RenameField(
            model_name='havebookstate',
            old_name='typename',
            new_name='statename',
        ),
        migrations.RenameField(
            model_name='haveclassify',
            old_name='typeid',
            new_name='classifyid',
        ),
        migrations.RenameField(
            model_name='haveclassify',
            old_name='typename',
            new_name='classifyname',
        ),
    ]
