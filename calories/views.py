from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'calories/index.html')


def catalog(request):
    return render(request, 'calories/catalog.html')


def counter(request):
    return render(request, 'calories/count.html')


def history(request):
    return render(request, 'calories/history.html')
