from django.shortcuts import render, redirect
from stock.models import Company, Stock
from django.urls import reverse
from .forms import StockForm

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
    comp = Company.objects.get(pk=pk)
    data = {
        'comp': comp,
    }
    return render(request, 'stock/detail_comp.html', data)

def item_new(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            post = form.save()
            # name = request.POST.get('name', None)
            # img = request.POST.get('img', None)
            # info = request.POST.get('info', None)
            # price = request.POST.get('price', None)
            # amount = request.POST.get('amoount', None)
            # company = request.POST.get('company', None)
            return redirect(reverse('detail_list'))
    else:
        form = StockForm()
    return render(request, 'stock/item_new.html', {'form': form})

def comp_new(request):
    return render(request, 'stock/comp_new.html')

