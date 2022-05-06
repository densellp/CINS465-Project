from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testPage(request):
    #return HttpResponse('Hurray, you made it to the test page!')
    return render(request, 'project/project.html')

def indexPage(request):
    return render(request, 'index.html')