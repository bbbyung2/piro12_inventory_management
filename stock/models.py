from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200, verbose_name='이름')
    tel = models.CharField(max_length=20, verbose_name='전화번호')
    addr = models.TextField(blank=True, verbose_name='주소')

    def __str__(self):
        return self.name
    

class Stock(models.Model):
    name = models.CharField(max_length=200, verbose_name='제품명')
    img = models.ImageField(blank=True, upload_to='images/', verbose_name='제품사진')
    info = models.TextField(blank=True, verbose_name='제품설명')
    price = models.PositiveIntegerField(verbose_name='가격')
    amount = models.IntegerField(verbose_name='남은수량')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='거래처', related_name='item')

    def __str__(self):
        return self.name
    