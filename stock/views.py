from django.shortcuts import render
from stock.models import Company, Stock
def item_list(request):
    # items = Stock.objects.all()
    # data = {
    #     'items': items  # 이름은 key를 따라감!!
    # }

    return render(request, 'stock/item_list.html')

def detail_list(request):
    return render(request, 'stock/detail_list.html')

def item_new(request):
    return render(request, 'stock/item_new.html')

