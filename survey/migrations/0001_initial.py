# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160104164526 on 2016-02-10 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_value', models.CharField(max_length=10)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(default=' ', max_length=200)),
                ('picture', models.ImageField(blank=True, upload_to='./images')),
                ('question_text', models.CharField(default=' ', max_length=200)),
                ('choice_one', models.CharField(blank=True, choices=[('not beautiful', 'not beautiful'), ('not easy', 'not user friendly')], max_length=200)),
                ('choice_seven', models.CharField(blank=True, choices=[('very beautiful', 'very beautiful'), ('very easy', 'very user friendly')], max_length=200)),
                ('question_type', models.IntegerField(choices=[(1, 1), (2, 2)], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Submit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Choice')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ManyToManyField(to='survey.Question'),
        ),
    ]
