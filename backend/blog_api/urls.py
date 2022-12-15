from .views import PostList
from rest_framework.routers import DefaultRouter
from .views import PostList, PostDetail, PostListDetailFilter
from django.urls import path


app_name = 'blog_api'
# router = DefaultRouter()
# router.register('', PostList, basename='post')

# urlpatterns = router.urls



urlpatterns = [
    path('posts/<str:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('search/', PostListDetailFilter.as_view(), name='postsearch'),
    path('', PostList.as_view(), name='listcreate'),
]