from django.shortcuts import render


# Create your views here.

class webpage():
    
        def landingpage(request):
            return render(request,'base.html')
    