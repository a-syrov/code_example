from django.db import models
import warnings
warnings.filterwarnings(
        'ignore', r"DateTimeField .* received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

# Create your models here.
class BashQuote(models.Model):
    rating = models.FloatField('Рейтинг', blank=True, default=1, null=True )
    quote_id = models.CharField('ID', max_length=200)
    date = models.DateTimeField('Дата')
    text = models.TextField('Цитата', max_length=5000)
    link = models.URLField('Ссылка на цитату')
    comics = models.URLField('Ссылка на комикс', blank=True, null=True, default=None)
    comics_img_url = models.URLField('Ссылка на изображение', blank=True, null=True, default=None)
    comics_image = models.ImageField('Комикс', upload_to='bash/comics', blank=True, default=None)
    is_comics = models.BooleanField('С комиксом')

    def __str__(self):
        return ("Цитата {} от {}.").format(self.id, self.date)

    class Meta:
        verbose_name='Цитата на главной'
        verbose_name='Цитаты на главной'
        ordering = ['-date']

        


class BashAbyssQuote(models.Model):
    quote_id = models.CharField('ID', max_length=200)
    date = models.DateTimeField('Дата')
    text = models.TextField('Цитата', max_length=5000)

    def __str__(self):
        return ("Цитата {} от {}.").format(self.id, self.date)

    class Meta:
        verbose_name='Цитата AbyssBest'
        verbose_name='Цитаты AbyssBest'
        ordering = ['-date']