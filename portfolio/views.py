from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
import requests

# Create your views here.

def home(request):
    response = ''
    url = 'http://127.0.0.1:8000/postList/'
    res = requests.get(url)
    if (res.status_code == 200):
        response = res.json()
        print(response)
    context = {
        'posts': response
    }
 
    return render(request, 'portfolio/home.html', context)


def about(request):
    return render(request, 'portfolio/about.html', {'title': 'About'})


@api_view(['GET'])
def postList(request):
    api_urls = { 
        'List':'/post-list/',
        'Detail View':'/post-detail/<str:pk>/',
        'Create':'/post-create/',
        'Update':'/post-update/<str:pk>/',
        'Delete':'/post-delete/<str:pk>/',
                
        
    }
    return Response(api_urls)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def postCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def postUpdate(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return Response('Posts deleted!')