# Generated by Django 2.2.1 on 2019-08-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleform', '0007_name_我要幾台iphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='我要幾台iphone',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]),
        ),
    ]
