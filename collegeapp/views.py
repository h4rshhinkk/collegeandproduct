from django.shortcuts import render

# Create your views here.
def fncollege(request):
    return render(request,'emea.html')
def fncourse(request): 
    return render(request,'newcourse.html')