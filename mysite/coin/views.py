from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import CoinType, Coin

# Create your views here.

class Index(generic.ListView):
    model = CoinType
    template_name = "coin/index.html"

### Coin Type Views ###

class CoinTypeDetail(generic.DetailView):
    model = CoinType
    template_name = "coin/CoinTypeDetail.html"

class CreateCoinType(generic.edit.CreateView):
    model = CoinType
    fields = '__all__'
    success_url = reverse_lazy('coin:index')

class CoinTypeDeleteView(generic.DetailView):
    model = CoinType
    template_name = "coin/CoinTypeDeleteView"

class DeleteCoinType(generic.edit.DeleteView):
    model = CoinType
    success_url = reverse_lazy('coin:index')

### Coin Views ###

class CoinDetail(generic.DetailView):
    model = Coin
    template_name = "coin/CoinDetail.html"

class CreateCoin(generic.edit.CreateView):
    model = Coin
    fields = '__all__'
    success_url = reverse_lazy('coin:index')

class CoinDeleteView(generic.DetailView): # list of coins with added delete button
    model = CoinType
    template_name = "coin/CoinDeleteView.html"

class DeleteCoin(generic.edit.DeleteView): # detletes the coin
    model = Coin
    success_url = reverse_lazy('coin:index')
