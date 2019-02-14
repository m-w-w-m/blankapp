from django.shortcuts import render
from .models import A
import random


def main(request):
	return render(request, 'mainapp/main.html')


def a(request):
	count = A.objects.count()
	randint = random.randint(1,count)
	item = A.objects.get(id=randint)
	items = A.objects.all()
	return render(request, 'mainapp/a.html', {'item': item, 'items': items})