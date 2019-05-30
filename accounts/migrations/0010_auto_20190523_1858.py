# Generated by Django 2.2 on 2019-05-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190523_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='userstatemodel',
            name='state_description',
            field=models.CharField(max_length=50, verbose_name='Stan użytkownika'),
        ),
    ]