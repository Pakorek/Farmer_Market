from django.shortcuts import render


def home(request):
    return render(request, 'farmer_market/home.html')
