# Generated by Django 3.2.13 on 2023-04-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_accounts', '0002_auto_20230410_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='twitter_account',
            name='description',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='twitter_account',
            field=models.CharField(max_length=128),
        ),
    ]