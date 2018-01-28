# Generated by Django 2.0 on 2018-01-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bashim', '0005_auto_20180102_1750'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bashabyssquote',
            options={'ordering': ['-date'], 'verbose_name': 'Цитаты AbyssBest'},
        ),
        migrations.AlterModelOptions(
            name='bashquote',
            options={'ordering': ['-date'], 'verbose_name': 'Цитаты на главной'},
        ),
        migrations.AddField(
            model_name='bashquote',
            name='comics_image',
            field=models.ImageField(blank=True, default=None, upload_to='bash/comics', verbose_name='Комикс'),
        ),
    ]
