from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор объявления',
                               related_name='ads', **NULLABLE)
    title = models.CharField(max_length=250, verbose_name='Название товара')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='ads/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return f'{self.author} - {self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор отзыва',
                               related_name='comments', **NULLABLE)
    ad = models.ForeignKey(to=Ad, on_delete=models.CASCADE, verbose_name='Объявление', related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return f'Комментарий {self.ad}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
