# Generated by Django 2.0 on 2018-01-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BashAbyssQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_id', models.CharField(max_length=200, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('text', models.TextField(max_length=5000, verbose_name='Цитата')),
            ],
        ),
        migrations.CreateModel(
            name='BashQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, default=1, null=True, verbose_name='Рейтинг')),
                ('quote_id', models.CharField(max_length=200, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('text', models.TextField(max_length=5000, verbose_name='Цитата')),
                ('link', models.URLField(verbose_name='Ссылка на цитату')),
                ('comics', models.URLField(verbose_name='Ссылка на комикс')),
                ('is_comics', models.BooleanField(verbose_name='С комиксом')),
            ],
        ),
    ]
