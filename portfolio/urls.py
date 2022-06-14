from django.urls import path
from .views import PostCreateView, PostDetailView, PostUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    # path('', views.home, name='api-overview'),
    path('postList/', views.postList, name='post-list'),
    path('postDetail/<str:pk>/', views.postDetail, name='post-detail'),
    path('postCreate/', views.postCreate, name='post-create'),
    path('postUpdate/<str:pk>/', views.postUpdate, name='post-update'),
    path('postDelete/<str:pk>/', views.postDelete, name='post-delete'),
    path('portfolio/create/', PostCreateView.as_view(), name='portfolio-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='portfolio-detail'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='portfolio-update'),


]   