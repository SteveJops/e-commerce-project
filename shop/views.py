from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):
    def get(self, request):
        return render(request, 'shop/home.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'shop/about.html')
