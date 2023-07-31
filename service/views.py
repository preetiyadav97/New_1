from django.shortcuts import render,HttpResponse

# Create your views here.
def first(request):
    return render(request, 'im.html')
