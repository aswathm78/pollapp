# Generated by Django 3.2 on 2022-07-22 13:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220722_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at '),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 22, 13, 46, 21, 295507, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
