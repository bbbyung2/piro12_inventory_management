from django.contrib import admin

# Register your models here.
from stock.models import Stock, Company

admin.site.register(Stock)
admin.site.register(Company)