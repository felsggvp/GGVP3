from django.shortcuts import render

# Create your views here.
def helloworld(request):
    return render(request, 'hello_world.html')
def oguzik(request):
    return render(request, 'oguzik.html')
def chuchu(request):
    return render(request, 'chuchu.html')