from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='이름')
    tel = models.CharField(max_length=20, verbose_name='전화번호')
    addr = models.TextField(blank=True, verbose_name='주소')


class Stock(models.Model):
    name = models.CharField(max_length=200, verbose_name='제품명')
    img = models.ImageField(blank=True, upload_to='images/', verbose_name='제품사진')
    info = models.TextField(blank=True, verbose_name='제품설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    amount = models.IntegerField(verbose_name='남은수량')
    company = models.ForeignKey('Company', on_delete=models.PROTECT)

