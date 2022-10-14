from django.shortcuts import render

# Create your views here.
def indexpersegi(request):
    return render(request, 'persegi.html')