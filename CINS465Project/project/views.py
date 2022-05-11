from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post
from django.contrib.auth.models import User
from .forms import postForm
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

#userlist = User.objects.all()
#postList = Post.objects.all()

def testPage(request):
    #return HttpResponse('Hurray, you made it to the test page!')
    msg1 = 'TestPage'
    number = 10
    context = {'msg1':msg1, 'number':number, 'testlist':testlist}
    return render(request, 'project/testpage.html', context)

def indexPage(request):
    userlist = User.objects.all()
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
    postList = Post.objects.all()
    msg5 = 'Main Feed'
    context = {'msg5':msg5, 'postList': postList}
    return render(request, 'mainfeed.html', context)

def Error404(request):
    msg6 = 'Error'
    context = {'msg6':msg6}
    return render(request, '404.html', context)

def createPost(request):
    form = postForm()

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('indexPage')

    context = {'form': form}
    return render(request, 'creat_post.html', context)

#def addLike(request):
    #tempPost = Post(instance=Post)
    #tempPost.likes = tempPost.likes + 1
    #return render(request, 'mainfeed.html')