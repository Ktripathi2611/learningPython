from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, serializers, status
from .models import Post
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class HelloView(APIView):
    def get(self, request):
        return Response({
            "message": "Hello, World!",
            "description": "Welcome to Django REST Framework!",
            "api_version": "1.0",
            "endpoints": {
                "hello": "/hello/ - This endpoint",
                "posts": "/post/ - List and create posts",
                "admin": "/admin/ - Django admin panel",
                "auth": "/api-auth/ - REST framework auth"
            }
        })


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_username',
                  'created_at', 'updated_at']
        read_only_fields = ['author', 'author_username', 'created_at', 'updated_at']


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'author__username': ['exact', 'icontains'],
        'created_at': ['exact', 'date', 'date__gte', 'date__lte'],
        'updated_at': ['exact', 'date', 'date__gte', 'date__lte'],
    }
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['title', 'created_at', 'updated_at', 'author__username']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]