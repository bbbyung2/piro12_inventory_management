from django import forms

from .models import Stock

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = ('name', 'img', 'info', 'price', 'amount', 'company')