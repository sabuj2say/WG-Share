# Generated by Django 4.2 on 2023-04-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wgshare',
            name='details',
            field=models.CharField(max_length=20, verbose_name='Details'),
        ),
    ]