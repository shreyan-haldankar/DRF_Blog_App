from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Create your views here.
class PostListView(generics.ListCreateAPIView):
    # Getting all the Posts that are published
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass



class PostDetailView(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer