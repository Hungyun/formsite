# Generated by Django 2.2.1 on 2019-08-12 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('googleform', '0011_auto_20190812_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='name',
            name='我想兌換的東西',
        ),
        migrations.AddField(
            model_name='name',
            name='驗證碼',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='驗證碼(密碼)'),
            preserve_default=False,
        ),
    ]
