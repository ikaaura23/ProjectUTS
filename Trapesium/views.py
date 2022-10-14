from django.shortcuts import render

# Create your views here.
def indextrapesium(request):
    return render(request, 'trapesium.html')