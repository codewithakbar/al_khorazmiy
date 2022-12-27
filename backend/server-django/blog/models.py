from django.db import models


class BIZ_HAQIMIZDA(models.Model):
    title = models.CharField(max_length=244, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Sarlavha ta\'rifi')
    
    class Meta:
        verbose_name = 'BIZ_HAQIMIZDA'
        verbose_name_plural = 'BIZ_HAQIMIZDA'


class BIZ_HAQIMIZDA_IMAGE(models.Model):
    biz_haqda = models.ForeignKey(BIZ_HAQIMIZDA, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        verbose_name = 'BIZ_HAQIMIZDA -> RASM TANLASH'
        verbose_name_plural = 'BIZ_HAQIMIZDA -> RASM TANLASH'

class ISH_JARAYONI(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        verbose_name = 'ISH JARAYONI'
        verbose_name_plural = 'ISH JARAYONI'

class PROEKTLARIMIZ(models.Model):
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        verbose_name = 'PROEKTLARIMIZ'
        verbose_name_plural = 'PROEKTLARIMIZ'

class Video(models.Model):
    video = models.FileField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videolar'

class IjtimoiyTarmoqLink(models.Model):
    telegram = models.CharField(max_length=244, verbose_name='Telegram Havolasi')
    instagram = models.CharField(max_length=244, verbose_name='Instagram Havolasi')
    youtube = models.CharField(max_length=244, verbose_name='Youtube Havolasi')
    
    class Meta:
        verbose_name = 'IJTIMOIY tarmoq havolasi'
        verbose_name_plural = 'IJTIMOIY tarmoq havolarali'
