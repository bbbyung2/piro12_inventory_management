from django.shortcuts import render
from stock.models import Company, Stock

def item_list(request):
    items = Stock.objects.all()
    data = {
        'items': items,
    }
    return render(request, 'stock/item_list.html', data)

def comp_list(request):
    comps = Company.objects.all()
    data = {
        'comps': comps,
    }
    return render(request, 'stock/comp_list.html', data)

def detail_list(request, pk):
    item = Stock.objects.get(pk=pk)
    data = {
        'item': item,
    }
    return render(request, 'stock/detail_list.html', data)

def detail_comp(request, pk):
    comp = Stock.objects.get(pk=pk)
    data = {
        'comp': comp,
    }
    return render(request, 'stock/detail.comp.html', data)

def item_new(request):
    return render(request, 'stock/item_new.html')

def comp_new(request):
    return render(request, 'stock/comp_new.html')

