# Generated by Django 2.0 on 2018-01-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bashim', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bashquote',
            name='rating',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='Рейтинг'),
        ),
    ]
