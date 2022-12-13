from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework import 
# Create your views here.






class PostUserWritePermission(BasePermission):
    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


# Model Viewsets
# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     # Custom get object
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     # Define a custom query set
#     def get_queryset(self):
#         return Post.objects.all()


# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     # Follows DRY principle
#     def list(self, request):
#         serializer_class  = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self,request,pk=None):
#         post = get_object_or_404(self.queryset, id=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)        



class PostList(generics.ListCreateAPIView):
    # Getting all the Posts that are published
    permission_classes = [IsAuthenticated]
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.filter(author=user)
        return queryset

class PostDetail(generics.ListAPIView):
    # permission_classes = [PostUserWritePermission]
    # queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_queryset(self):
    #     slug = self.kwargs['pk']
    #     queryset = Post.objects.filter(id=slug)
    #     return queryset

    # To get query params we have request.query_params.get
    def get_queryset(self):
        slug = self.request.query_params.get("slug", None)
        return Post.objects.filter(slug=slug)

class PostListDetailFilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # Search filter methods
    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.
    filter_backend = [filters.SearchFilter]
    search_fields = ['^slug']