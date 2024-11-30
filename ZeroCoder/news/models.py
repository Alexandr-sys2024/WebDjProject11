from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=200)
    short_description = models.TextField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)  # Автоматическая установка времени публикации
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')  # Добавляем автора новости

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


#