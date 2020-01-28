from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView

from stock.models import Company, Stock
from django.urls import reverse
from .forms import StockForm, CompanyForm


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

# def item_new(request, item=None):
#     if request.method == 'POST':
#         # name = request.POST.get('name', None)
#         # img = request.POST.get('img', None)
#         # info = request.POST.get('info', None)
#         # price = request.POST.get('price', None)
#         # amount = request.POST.get('amoount', None)
#         # company = request.POST.get('company', None)
#         form = StockForm(request.POST, request.FILES, instance=item)
#         # data = request.POST
#         # files = request.FILES
#
#         if form.is_valid():
#             item = form.save()
#
#             return redirect(reverse('detail_list', item.pk))
#     else:
#         form = StockForm(instance=item)
#     return render(request, 'stock/item_new.html', {'form': form})

item_new = CreateView.as_view(model=Stock, form_class=StockForm)

item_edit = UpdateView.as_view(model=Stock, form_class=StockForm)

comp_new = CreateView.as_view(model=Company, form_class=CompanyForm)

comp_edit = UpdateView.as_view(model=Company, form_class=CompanyForm)
#
# def comp_new(request, com=None):
#     if request.method == 'POST':
#         name = request.POST.get('name', None)
#         tel = request.POST.get('tel', None)
#         addr = request.POST.get('addr', None)
#         if name and tel and addr:
#             com = Company.objects.create(
#                 name=name,
#                 tel=tel,
#                 addr=addr
#             )
#             return redirect('stock:detail_comp', com.pk)
#     return render(request, 'stock/comp_new.html')

# def item_edit(request, pk):
#     item = Stock.objects.get(pk=pk)
#     if request.method == 'GET':
#         return render(request, 'stock/stock_form.html', {'item': item})
#     elif request.method == 'POST':
#         name = request.POST.get('name', None)
#         img = request.POST.get('img', None)
#         info = request.POST.get('info', None)
#         price = request.POST.get('price', None)
#         amount = request.POST.get('amount', None)
#         company = request.POST.get('company', None)
#
#         item.name = name
#         item.img = img
#         item.info = info
#         item.price = price
#         item.amount = amount
#         item.company = company
#
#         item.save()
#         return redirect('stock:detail_list', item.pk)

def item_del(request, pk):
    item = Stock.objects.get(pk=pk)
    item.delete()
    return redirect('stock:item_list')

# def comp_edit(request, pk):
#     comp = Company.objects.get(pk=pk)
#     if request.method == 'GET':
#         return render(request, 'stock/company_form.html', { 'comp': comp})
#     elif request.method == 'POST':
#         name = request.POST.get('name', None)
#         tel = request.POST.get('tel', None)
#         addr = request.POST.get('addr', None)
#
#         comp.name = name
#         comp.tel = tel
#         comp.addr = addr
#
#         comp.save()
#         return redirect('stock:detail_comp', comp.pk)

def comp_del(request, pk):
    comp = Company.objects.get(pk=pk)
    comp.delete()
    return redirect('stock:comp_list')

def item_add(requeset, pk):
    item = Stock.objects.get(pk=pk)

