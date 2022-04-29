# Generated by Django 3.2.13 on 2022-04-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinejudge', '0004_submission'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='answers',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='testcases',
        ),
        migrations.AddField(
            model_name='problem',
            name='testinput1',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testinput2',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testinput3',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testinput4',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testinput5',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testoutput1',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testoutput2',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testoutput3',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testoutput4',
            field=models.TextField(default='n'),
        ),
        migrations.AddField(
            model_name='problem',
            name='testoutput5',
            field=models.TextField(default='n'),
        ),
    ]
