# Generated by Django 2.2.5 on 2019-09-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibMysql', '0012_auto_20190906_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='intro',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobile',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='qq',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='weibo',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
