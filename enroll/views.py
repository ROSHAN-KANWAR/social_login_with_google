from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')

def Profile(request):
    return render(request,'profile.html')