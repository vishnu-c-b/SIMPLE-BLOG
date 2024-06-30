from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Q

from .models import Post

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
        return redirect('login')
    return render(request, 'register.html')

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return redirect('list_posts')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
@csrf_protect
def create_post(request):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.create(
            title=data['title'],
            content=data['content'],
            author=request.user
        )
        return redirect('read_post', post_id=post.id)
    return render(request, 'create_post.html')

def list_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-publication_date')
    else:
        posts = Post.objects.all().order_by('-publication_date')

    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_posts.html', {'posts': page_obj, 'page_obj': page_obj, 'paginator': paginator})

def read_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'read_post.html', {'post': post})

@login_required
def my_posts(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-publication_date')

    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_posts.html', {'posts': page_obj, 'page_obj': page_obj, 'paginator': paginator})

@login_required
@csrf_protect
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        data = request.POST
        post.title = data['title']
        post.content = data['content']
        post.save()
        return redirect('read_post', post_id=post.id)
    return render(request, 'update_post.html', {'post': post})

@login_required
@csrf_protect
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        post.delete()
        return redirect('list_posts')
    return render(request, 'delete_post.html', {'post': post})
