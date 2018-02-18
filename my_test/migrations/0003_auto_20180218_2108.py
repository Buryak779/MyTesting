# Generated by Django 2.0.2 on 2018-02-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_test', '0002_auto_20180218_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytest',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='mytest',
            name='moderation',
            field=models.BooleanField(default=False, verbose_name='Модерация'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='answer_1',
            field=models.CharField(max_length=100, verbose_name='Вариант1'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='answer_2',
            field=models.CharField(max_length=100, verbose_name='Вариант2'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='answer_3',
            field=models.CharField(max_length=100, verbose_name='Вариант3'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='question',
            field=models.TextField(max_length=270, verbose_name='Вопрос'),
        ),
    ]
