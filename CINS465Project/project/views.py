from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

testlist = [
    {
        'id': '1',
        'title': "test file 1",
        'description': 'this is test file 1',
    },
    {
        'id': '2',
        'title': "test file 2",
        'description': 'this is test file 2',
    },
    {
        'id': '3',
        'title': "test file 3",
        'description': 'this is test file 3',
    },
]

def testPage(request):
    #return HttpResponse('Hurray, you made it to the test page!')
    msg1 = 'TestPage'
    number = 10
    context = {'msg1':msg1, 'number':number, 'testlist':testlist}
    return render(request, 'project/testpage.html', context)

def indexPage(request):
    msg2 = 'Index'
    context = {'msg2':msg2}
    return render(request, 'index.html', context)