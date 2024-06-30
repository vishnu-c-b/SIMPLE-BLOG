from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from blog.models import Post
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# Authentication API

@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.data
        try:
            user = User.objects.create_user(username=data['username'], email=data['email'], password=data['password'])
            return JsonResponse({'message': 'User registered successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        data = request.data
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return JsonResponse({'message': 'User logged in successfully', 'token': token.key})
        return JsonResponse({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'User logged out successfully'})
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


# CRUD Operations
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == 'POST':
        data = request.data
        try:
            post = Post.objects.create(
                title=data['title'],
                content=data['content'],
                author=request.user
            )
            return JsonResponse({'message': 'Post created successfully', 'post_id': post.id})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-publication_date')
    else:
        posts = Post.objects.all().order_by('-publication_date')

    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    post_list = [{'title': post.title, 'content': post.content, 'author': post.author.username} for post in page_obj]
    return JsonResponse({'posts': post_list, 'page': page_obj.number, 'pages': paginator.num_pages})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def read_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post_data = {'title': post.title, 'content': post.content, 'author': post.author.username , 'publication_date': post.publication_date}
    return JsonResponse(post_data)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return JsonResponse({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        data = request.data
        try:
            post.title = data['title']
            post.content = data['content']
            post.save()
            return JsonResponse({'message': 'Post updated successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.author:
        return JsonResponse({'message': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        try:
            post.delete()
            return JsonResponse({'message': 'Post deleted successfully'})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({'message': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
