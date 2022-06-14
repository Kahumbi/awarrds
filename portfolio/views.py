from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
import requests
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView

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
        # get all the posts
        # serialize all posts
        # return json
    posts = Post.objects.all().order_by('-id')
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

class PostCreateView(LoginRequiredMixin,CreateView):
    model= Post
    fields = ['title', 'content', 'image', 'link']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post 
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def search_post(request):
    posts = ''
    query = request.GET.get('query')
    if query != None:
        posts = Post.objects.filter(title__contains=query)

    context = {
    'posts': posts,
    'title':'search posts'
}

    return render(request, 'portfolio/search.html', context)