from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User
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

userlist = User.objects.all()

def testPage(request):
    #return HttpResponse('Hurray, you made it to the test page!')
    msg1 = 'TestPage'
    number = 10
    context = {'msg1':msg1, 'number':number, 'testlist':testlist}
    return render(request, 'project/testpage.html', context)

def indexPage(request):
    msg2 = 'Index'
    #print(userlist)
    usernames = []
    for i in userlist:
        usernames.append(i.username)
    context = {'msg2':msg2, 'usernames':usernames}
    return render(request, 'index.html', context)

def loginPage(request):
    msg3 = 'Login'
    context = {'msg3':msg3}
    return render(request, 'login.html', context)

def profilePage(request):
    msg4 = 'Account'
    context = {'msg4':msg4}
    return render(request, 'profilepage.html', context)

def mainFeed(request):
    msg5 = 'Main Feed'
    context = {'msg5':msg5}
    return render(request, 'mainfeed.html', context)

def Error404(request):
    msg6 = 'Error'
    context = {'msg6':msg6}
    return render(request, '404.html', context)