from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile, Post, Comment
from django.contrib.auth.models import User
from .forms import commentForm, postForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
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

@login_required(login_url="loginPage")
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

#def loginPage(request):
    #msg3 = 'Login'
    #context = {'msg3':msg3}
    #return render(request, 'login.html', context)

@login_required(login_url="loginPage")
def profilePage(request):
    msg4 = 'Account'
    context = {'msg4':msg4}
    return render(request, 'profilepage.html', context)

@login_required(login_url="loginPage")
def mainFeed(request):
    postList = Post.objects.all()
    commentList = Comment.objects.all()
    postList.reverse()
    msg5 = 'Main Feed'
    context = {'msg5':msg5, 'postList': postList, 'commentList': commentList}
    return render(request, 'mainfeed.html', context)

def Error404(request):
    msg6 = 'Error'
    context = {'msg6':msg6}
    return render(request, '404.html', context)

@login_required(login_url="loginPage")
def createPost(request):
    form = postForm()
    #form.profile = request.user
    profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.save()
            return redirect('indexPage')

    context = {'form': form, 'profile': profile}
    return render(request, 'creat_post.html', context)

@login_required(login_url="loginPage")
def createComment(request, pk):
    form = commentForm()
    profile = Profile.objects.get(user = request.user)
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.profile = profile
            comment.post = post
            comment.save()
            return redirect('mainFeed')

    context = {'form': form, 'profile': profile, 'post': post}
    return render(request, 'makecomment.html', context)

def addLike(request, pk):
    post = Post.objects.get(id=pk)
    post.likes += 1
    post.save()
    return redirect('mainFeed')

def loginPage(request):
    page = 'login'
    msg3 = 'Login'
    context = {'msg3':msg3, 'page':page}

    if request.user.is_authenticated:
        return redirect('Error404')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request, 'Username does not exist')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in')
                return redirect('indexPage')
            else:
                messages.error(request, 'Username OR Password is incorrect')

        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.success(request, 'You have logged out')
    return redirect('loginPage')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            profile = Profile()
            profile.user = user
            user.save()
            profile.save()

            messages.success(request, 'User account created successfully!')
            return redirect('indexPage')

        else:
            messages.error(request, 'An unknown error occured!')

    context = {'page': page, 'form': form}
    return render(request, 'login.html', context)

# Dedicated to Justin Peters, Rest in Peace 2000-2022