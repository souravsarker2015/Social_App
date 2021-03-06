# Generated by Django 3.2.6 on 2021-10-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='profile'),
        ),
    ]
