# Generated by Django 2.0 on 2018-09-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20180912_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='matches',
            new_name='match_id',
        ),
    ]
