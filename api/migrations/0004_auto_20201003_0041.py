# Generated by Django 3.1.1 on 2020-10-03 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201002_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(max_length=280),
        ),
    ]
