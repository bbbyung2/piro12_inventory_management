from django import forms

from .models import Stock, Company

class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

