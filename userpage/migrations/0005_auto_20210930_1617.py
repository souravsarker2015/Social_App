# Generated by Django 3.2.6 on 2021-09-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0004_auto_20210930_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='connection',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='follower',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.IntegerField(default=0),
        ),
    ]
