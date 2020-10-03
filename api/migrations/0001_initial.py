# Generated by Django 3.1.1 on 2020-09-30 19:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_type', models.CharField(choices=[('Boast', 'Boast'), ('Roast', 'Roast')], max_length=5)),
                ('content', models.CharField(max_length=250)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_votes', models.IntegerField(default=0)),
            ],
        ),
    ]