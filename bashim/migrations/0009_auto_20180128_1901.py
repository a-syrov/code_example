# Generated by Django 2.0 on 2018-01-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bashim', '0008_auto_20180128_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bashquote',
            name='rating',
            field=models.FloatField(blank=True, default=1, null=True, verbose_name='Рейтинг'),
        ),
    ]