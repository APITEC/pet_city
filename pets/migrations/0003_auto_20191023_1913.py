# Generated by Django 2.2.6 on 2019-10-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20191023_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtype',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
