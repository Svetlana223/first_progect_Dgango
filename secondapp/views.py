from django.shortcuts import render, HttpResponse
from django.views import View

class IndexPageView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello, world</h1>')
