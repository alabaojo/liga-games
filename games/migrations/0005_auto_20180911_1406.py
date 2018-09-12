# Generated by Django 2.1.1 on 2018-09-11 14:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_auto_20180911_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('match_order',),
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goal', models.IntegerField()),
                ('away_goal', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='fixture',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='season',
            name='team_id',
        ),
        migrations.AddField(
            model_name='season',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 11, 14, 6, 2, 740076, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='season',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 11, 14, 6, 2, 740035, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Fixture',
        ),
        migrations.AddField(
            model_name='match',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Result'),
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(to='games.Team'),
        ),
        migrations.AddField(
            model_name='season',
            name='matches',
            field=models.ManyToManyField(to='games.Match'),
        ),
    ]
