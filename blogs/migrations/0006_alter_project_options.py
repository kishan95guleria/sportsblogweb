# Generated by Django 3.2.7 on 2021-09-27 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20210918_1904'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
