# Generated by Django 3.2.7 on 2021-10-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_auto_20211011_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
